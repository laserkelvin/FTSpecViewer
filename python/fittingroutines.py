import peakutils
from scipy.optimize import curve_fit
from scipy import constants
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


def doppler_pair(x, A1, A2, W1, W2, center, doppler_splitting, offset):
    """ Function for a pair of Doppler peaks """
    return lorentzian_func(x, A1, center - doppler_splitting, W1, offset) + \
           lorentzian_func(x, A2, center + doppler_splitting, W2, offset)


def arb_doppler_func(x, *params):
    """ 
         Fit an arbitrary number of Doppler pairs to data.

         The argument params is given as a list of dictionaries,
         each of which has the parameters for a particular Doppler
         pair.
    """
    y = np.zeros(len(x))
    for i in range(0, len(params), 7):
        last_pos = i + 7
        y+=doppler_pair(x, *params[i:last_pos])
    return y


def fit_doppler_pair(fft_df, center=None):
    if "Fit" not in list(fft_df.keys()):
        fft_df["Fit"] = np.zeros(len(fft_df["Frequency"]))
    if center is not None:
        # If a center is provided as a list of frequencies, take the average
        center = np.average(center)
    elif center is None:
        # If no center guess, take center of the frequency window
        center = (fft_df["Frequency"].min() + fft_df["Frequency"].max()) / 2.
    initial = [5e-2, 5e-2, 0.01, 0.01, center, 0.001, 0.]
    bounds = (
        [0., 0., 1e-4, 1e-4, center - 0.01, 0., -np.inf],
        [np.inf, np.inf, 0.025, 0.025, center + 0.01, 1.0, np.inf]
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


class FitModel:
    """
       FitModel class

       This class acts as a medium between the spectral data, and a way
       to actually fit the data in a flexible/physically meaningful manner.

       This class will handle the number of Doppler peaks, and whatever
       physical parameters that may be relevant (e.g. inert gas, radical)
       in determining the line shape and fitting parameters.
       Using these attributes, a fitting function will be dynamically
       generated that can be fit to using a class method. The derived
       parameters will be formatted before handing it back to the main
       program.
    """
    def __init__(self, guess_frequencies):
        self.param_list = list()
        self.guess_frequencies = guess_frequencies
        self.model_func = None
        self.model = np.array([])
        self.npairs = 0
        if len(self.guess_frequencies) > 0:
            self.npairs = len(self.guess_frequencies)
        self.gas = "Ne"
        self.radical = False

    def fit_model(self, xdata, ydata):
        # Wrapper for the scipy curve_fit call
        if self.model_func is None:
            self.generate_func_input()
        try:
            self.opt, self.cov = curve_fit(
                self.model_func,
                xdata,
                ydata,
                p0=self.param_list,
                bounds=self.boundary_list
            )
            self.format_results()
            self.model = arb_doppler_func(
                xdata,
                *self.opt
            )
        except RuntimeError:
            # If the fitting fails, return None
            self.opt, self.cov, self.results = None

    def generate_params(self):
        # Function to generate a dictionary of parameters using
        # class attributes
        param_dict = {
            "A1": 1e-2,
            "A2": 1e-2,
            "offset": 0.
        }
        # Calculate the Doppler splitting depending on what gas is used
        param_dict["doppler_splitting"] = self.calculate_doppler()
        # Fat peaks for radicals
        if self.radical is True:
            param_dict["W1"] = 0.05
            param_dict["W2"] = 0.05
        else:
            param_dict["W1"] = 0.025
            param_dict["W2"] = 0.025
        return param_dict

    def generate_func_input(self):
        # Function that will generate the model function, including
        # the initial guess for parameters and the boundary conditions
        self.param_list = list()
        self.boundary_list = list()
        # Parameters
        upper_bounds = list()
        lower_bounds = list()
        for index, frequency in enumerate(self.guess_frequencies):
            param_dict = self.generate_params()
            param_dict["center"] = frequency
            param = [param_dict[key] for key in ["A1", "A2", "W1", "W2", \
                                                 "center", "doppler_splitting", \
                                                 "offset"]]
            self.param_list.append(param)
            upper_bounds.append(
                [
                    np.inf,  # A1
                    np.inf,  # A2
                    param_dict["W1"] + 0.01,   # W1
                    param_dict["W2"] + 0.01,   # W2
                    param_dict["center"] + 0.1,
                    param_dict["doppler_splitting"] + 0.05,
                    np.inf
                ]
            )
            lower_bounds.append(
                [
                    0.,  # A1
                    0.,  # A2
                    param_dict["W1"] - 0.01,   # W1
                    param_dict["W2"] - 0.01,   # W2
                    param_dict["center"] - 0.1,
                    param_dict["doppler_splitting"] - 0.05,
                    -np.inf
                ]
            )
        upper_bounds = flatten_list(upper_bounds)
        lower_bounds = flatten_list(lower_bounds)
        self.boundary_list = (lower_bounds, upper_bounds)
        self.param_list = flatten_list(self.param_list)
        self.model_func = arb_doppler_func

    def format_results(self):
        # Class method for taking the results of the fit and
        # actually formatting them into a presentable dictionary
        self.results = dict()
        param_names = ["A1", "A2", "W1", "W2", "center", "doppler_splitting", "offset"]
        self.variance = np.sqrt(np.diag(self.cov))
        # Calculate the uncertainties of the parameters
        if self.opt is not None:
            for index, i in enumerate(range(0, len(self.opt), 7)):
                self.results[index] = dict()
                for position, key in enumerate(param_names):
                   self.results[index][key] = ufloat(
                       self.opt[i + position],
                       self.variance[i + position]
                   )

    def calculate_doppler(self):
        # Function for approximating the Doppler splitting based
        # on the inert gas used in the expansion
        # I assume a velocity of 1800 m/s for helium, and that the
        # kinetic energy is the same regardless of the gas used.
        # The Doppler shift is calculated for a frequency of 10 GHz.
        if self.gas == "H2":
            mass = 2.016
        elif self.gas == "He":
            mass = 4.0026
        elif self.gas == "Ne":
            mass = 20.1797
        elif self.gas == "Ar":
            mass = 39.948
        elif self.gas == "Kr":
            mass = 83.798
        elif self.gas == "Xe":
            mass = 131.29

        if len(self.guess_frequencies) > 0:
            # If frequencies are available, get the guess from them
            frequency = np.average(self.guess_frequencies)
        else:
            # Otherwise, default to 10 GHz
            frequency = 10000.
        # Assuming same kinetic energy, calculate velocity
        velocity = ((4.0026 * 1800.**2.) / mass)**0.5
        # Calculate frequency shift in MHz
        shift = (velocity * frequency) / constants.c
        return shift

