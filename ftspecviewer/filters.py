"""
    Routines for special filtering cases.

"""

from scipy import signal as spsig
import numpy as np


def butter_bandpass(lowcut, highcut, fs, order=5):
    """
        A modified version of the Butterworth bandpass filter described here,
        adapted for use with the FID signal.
        http://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html
        The arguments are:

        lowcut -
            The low frequency cut-off, given in Hertz.
        highcut -
            The high frequency cut-off, given in Hertz.
        fs -
            The sampling rate, given in Hertz. From the FIDs, this means that
            the inverse of the FID spacing is used.
    """
    nyq = 0.5 * (fs / (2. * np.pi))
    low = (lowcut * 1e3) / nyq
    high = (highcut * 1e3) / nyq
    b, a = spsig.butter(order, [low, high], btype='band', analog=False)
    return b, a


def apply_butter_filter(data, lowcut, highcut, fs, order=5):
    """
        A modified Butterworth bandpass filter, adapted from the Scipy cookbook.

        The argument data supplies the FID, which then uses the scipy signal
        processing function to apply the digital filter, and returns the filtered
        FID.

        See the filter function above for additional arguments.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = spsig.lfilter(b, a, data)
    return y
