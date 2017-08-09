import peakutils
from scipy.optimize import curve_fit
import numpy as np

def find_peaks(xdata, ydata, thres=0.3):
    # Finds the peak intensities in ydata, and returns the
    # corresponding frequencies
    indexes = peakutils.indexes(ydata, thres=thres)
    peak_frequencies = xdata[indexes]
    return peak_frequencies

def center_cavity(xdata, ydata, thres):
    # Calculates the center cavity frequency by taking the average
    # of the two Doppler horns
    center = np.average(find_peaks(xdata, ydata, thres))
    return center

def gaussian_func(x, a, c, w, offset):
    # A stock Gaussian lineshape function
    return a / np.sqrt(2. * np.pi * w**2.) * np.exp(-(x - c)**2. / 2. * w**2) + offset

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
