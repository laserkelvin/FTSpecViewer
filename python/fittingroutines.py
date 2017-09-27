import peakutils
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy
import numpy as np


def find_peaks(xdata, ydata, thres=0.3, min_dist=1):
    # Finds the peak intensities in ydata, and returns the
    # corresponding frequencies
    indexes = peakutils.indexes(ydata, thres=thres)
    peak_frequencies = np.array(xdata[indexes].astype(float))
    peak_intensities = np.array(ydata[indexes].astype(float))
    return peak_frequencies, peak_intensities


def center_cavity(xdata, ydata, thres):
    # Calculates the center cavity frequency by taking the average
    # of the two Doppler horns
    center, intensity = np.average(find_peaks(xdata, ydata, thres), axis=1)
    return center, intensity


def gaussian_func(x, amplitude, center, width, offset):
    # Stock Gaussian
    return amplitude / np.sqrt(width**2. * 2. * np.pi) * (np.exp(-(x - center)**2. / (2. * width**2.))) + offset


def lorentzian_func(x, amplitude, center, width, offset):
    # Stock Lorenztian
    return amplitude / np.pi * (0.5 * width)/((x - center)**2. + (0.5 * width)**2.)


def arb_gaussian_func(x, *params):
    """ Fit an arbtirary number of Gaussian line profiles to data.
        The parameters are given in lots of three; the amplitude,
        center, and width of each line.
    """
    y = np.zeros(len(x))
    for i in range(0, len(params), 4):
        amplitude = params[i]
        center = params[i+1]
        width = params[i+2]
        offset = params[i+3]
        y += gaussian_func(x, amplitude, center, width, offset)
    return y


def doppler_pair(x, a1, a2, w1, w2, center, doppler_splitting, offset):
    """ Function for a pair of Doppler peaks """
    return lorentzian_func(x, a1, center - doppler_splitting, w1, offset) + \
           lorentzian_func(x, a2, center + doppler_splitting, w2, offset)


def fit_doppler_pair(fft_df, center=None):
    if "Fit" not in list(fft_df.keys()):
        fft_df["Fit"] = np.zeros(len(fft_df["Frequency"]))
    if center is not None:
        # If a center is provided as a list of frequencies, take the average
        center = np.average(center)
    elif center is None:
        # If no center guess, take center of the frequency window
        center = (fft_df["Frequency"].min() + fft_df["Frequency"].max()) / 2.
    initial = [0.5, 0.5, 0.01, 0.01, center, 0.001, 0.]
    bounds = (
        [0., 0., 1e-4, 1e-4, center - 0.01, 0., -np.inf],
        [np.inf, np.inf, 0.016, 0.016, center + 0.01, 0.1, np.inf]
    )
    # Call the scipy fitting wrapper
    popt, pcov = curve_fit(
        doppler_pair,
        fft_df["Frequency"],
        fft_df["Intensity"],
        p0=initial,
        bounds=bounds
    )

    fft_df["Fit"] += doppler_pair(fft_df["Frequency"], *popt)
    fit_results = dict()
    sigmas = np.sqrt(np.diag(pcov))
    names = ["A1", "A2", "W1", "W2", "Frequency", "Doppler-width", "Offset"]
    for name, value, sigma in zip(names, popt, sigmas):
        fit_results[name] = ufloat(value, sigma)
    return fit_results


def fit_lineshape(func, xdata, ydata, peak_guesses=None):
    """ A wrapper for curve_fit function of SciPy.
        Necessary arguments are the fitting function, and the data you want
        to fit.
        The `peak_guesses` argument can be supplied with a list of guesses for
        peak locations. These will be used to calculate boundary conditions for
        the fit.

        The boundary conditions are hardcoded to reasonable values - for example,
        center values cannot be +/-1 MHz away from the initial guess. Similarly,
        the width of peaks cannot be excessively large.
    """
    if peak_guesses is not None:
        # The case for multiple lines being fit
        initial = flatten_list(
            [value for value in [[1., center, 0.01, 0.] for center in peak_guesses]]
        )
        bounds = (
            flatten_list([value for value in [[1e-3, center - 0.5, 1e-5, -1e-3] for center in peak_guesses]]),
           flatten_list([value for value in [[np.infty, center + 0.5, 0.05, 1e3] for center in peak_guesses]])
         )
    else:
        initial = None
        bounds = None
    # Perform the curve_fit
    popt, pcov = curve_fit(
        func,
        xdata,
        ydata,
        p0=initial,
        bounds=bounds
    )
    # Return the diagonal of the covariance matrix
    pcov = np.diag(pcov)
    return popt, pcov


def flatten_list(nested_list):
    # Silly little function that will flatten a nested list into a single list
    # This is used for generating initial parameters for multi-lineshape fits
    flattened_list = list()
    for sublist in nested_list:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list
