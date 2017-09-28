# FTSpecViewer

## A PyQt5 application written for microwave spectroscopy analysis

---

## Introduction

FTSpecViewer was written to assist in the interactive and exploratory analysis of microwave spectra. While there are many proprietary programs that are capable of performing the similar analyses (such as Origin and Igor) there are few that are specialized; filtering and fitting, for example, can be routinely done with these programs, however support for techniques such as double resonance and overlaying catalog spectra are not as well accounted for.

FTSpecViewer was written to be open source -- hence the choice of Qt and Python. Please feel free to make any modifications and contributions to the code. For now, I've tried to minimize the number of additional packages required for the sake of portability, but we will see how far the program develops.

Usage is pretty straightforward - load an experimental spectrum, look for peaks, get quantitative values, etc.

The font used throughout the program is Roboto - freely available from the Google open source font repository: http://www.fonts.google.com

The icons used are pulled from the Open Iconic project: https://useiconic.com/open

## Features

- Loading and reading general ASCII spectra (tab delimited) and support for additional file types, such as SPFIT/SPCAT.

- Signal processing routines, such as window functions and various filters.

- Overlay catalog spectra to assist with assignment.

- Fit double resonance depletion data, and report the uncertainties from the fit.

- Interactivity!

## To-do

- Point-and-click peaks, and corresponding fits to extract spectroscopic parameters

- More sophisticated signal processing routines (e.g. matched filters)

- Multidimensional spectral analysis; time evolution of chirped-pulse spectra

- HDF5 compression of data

- External calls to SPCAT/SPFIT

---

## Installing and running FTSpecViewer

A rudimentary script in the type folder is called `setup.py` - this is _not_ a `setup_tools` or `pip`-able script, but rather a quick and dirty way to ensure the required packages are installed with the Python distribution used. I would personally recommend installing Anaconda as the preferred distro. Simply run the script by calling: `python setup.py` in the top folder. The program should then be run via command line by calling `python app.py`, which is a script in the `python/` folder that drives the application.

I have interest in packaging the program for distribution using more elegant solutions, but since development is still in early stages the focus is more on completing functionality.

---

## Notes on implementation

### FFT and signal processing

The numerical routines are primarily based on NumPy and SciPy routines. The FFT functions rely on those from NumPy, while the signal processing (i.e. filtering, window functions) use the `signal` modules from SciPy.

The order of business is:
1. Read in FID, stored as an attribute of the `FTData` class
2. Apply a digital 5th order Butterworth band-pass filter. This requires low- and high-frequency cut-offs to be provided.
    - The sampling rate of the FID is required, as the inverse of the FID spacing. While this is given in Hertz, this is converted to radians/second in order for it to be used in the `signal.butter` function.
    - As a note of comparison, the high-pass filter in QtFTM is a linear RC filter.
3. Apply a delay padding to the FID - this sets the signal to zero for a specified number of microseconds at the beginning of the FID.
4. Apply a window function to the signal with those available in `scipy.signal.get_window`. Typical functions are the Hanning and Blackman-Harris filters.
5. Apply an exponential filter using `scipy.signal.exponential`
6. Perform the FFT.

### Peak detection

The peak finding is done using the `peakutils` routines. Simple as that.

### Uncertainties

Because I'm lazy and bad with estimating uncertainty, I rely on the `uncertainties` package to perform the error propagation in routines where fitting is done. The covariance matrix from `curve_fit` is used to estimate the variance, which is then packaged together with the optimized parameter as a `ufloat`.
