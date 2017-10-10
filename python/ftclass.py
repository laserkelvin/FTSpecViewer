import numpy as np
import pandas as pd
from scipy import signal as spsig
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from uncertainties import ufloat, unumpy
import peakutils
import os
from glob import glob

from fittingroutines import gaussian_func
from filters import *
from parsers import parse_batch, parse_fid


class FTData:
    """ A general class for processing FTMW and FTCP data.
        A file is specified, with the argument `fid` that will determine
        whether or not the data being loaded is an FID, or a tab delimited
        frequency/intensity spectrum.

        This class needs serious cleaning up and reorganizing. Ideally, the
        parsing should be done in a separate, general function.
    """
    def __init__(self, filepath=None, fid=False, mmw=False):
        self.settings = dict()
        self.settings["Calibration"] = False
        if fid is True:
            if len(filepath) == 1:
                self.settings, self.fid = parse_fid(filepath[0], mmw)
                self.fid = np.array(self.fid)
            elif len(filepath) > 1:
                # For multi-FIDs, we want to co-average them
                self.fids_bin = list()
                for file in filepath:
                    self.settings, fid = parse_fid(file, mmw)
                    self.fids_bin.append(fid)
                self.fid = np.average(self.fids_bin, axis=0)
        else:
            try:
                self.spectrum = pd.read_csv(
                    filepath,
                    sep=None,
                    delimiter=None,
                    skiprows=1,
                    names=["Frequency", "Intensity"]
                )
            except ValueError:
                raise FileParseError("Cannot parse spectrum!")

    def fid2fft(self, window_function=None, band_pass=None, exp_filter=None, delay=None):
        """ Perform the DFT of an FID using NumPy's FFT package. """
        available_windows = [
            "blackmanharris",
            "blackman",
            "boxcar",
            "gaussian",
            "hanning",
            "bartlett"
        ]
        self.spectrum = None
        self.fid_df = None
        # Make a copy of the original FID
        proc_fid = np.copy(self.fid)
        if band_pass is not None:
            # Apply a band-pass filter to the FID signal.
            if band_pass[0] < band_pass[1]:
                # Make sure the low pass frequency doesn't exceed the high pass
                proc_fid = apply_butter_filter(
                    proc_fid,
                    band_pass[0],
                    band_pass[1],
                    1. / self.settings["FID spacing"]
                )
        # Set the FID time points to zero
        if delay is not None and delay > 0.:
            proc_fid[:int(delay)] = 0.
        # Use a scipy.signal window function to process the FID signal
        if window_function is not None and window_function != "none":
            if window_function not in available_windows:
                print("Incorrect choice for window function.")
                print("Available:")
                print(available_windows)
            else:
                proc_fid *= spsig.get_window(window_function, proc_fid.size)
        # Apply the exponential filter to smooth
        if exp_filter is not None and exp_filter > 0.:
            proc_fid *= spsig.exponential(proc_fid.size, tau=exp_filter)
        # Perform the FFT
        amplitude = np.fft.fft(proc_fid)

        time = np.linspace(
            0.,
            self.settings["FID spacing"] * self.settings["FID points"],
            self.settings["FID points"]
        )

        freq = np.arange(proc_fid.size / 2, dtype=float) / proc_fid.size / self.settings["FID spacing"]
        amplitude = np.abs(amplitude[:int(proc_fid.size / 2)]) / proc_fid.size

        # Calclate the frequency window
        frequency = np.linspace(
            self.settings["Probe frequency"],
            self.settings["Probe frequency"] + 1.,
            amplitude.size
        )
        self.spectrum = pd.DataFrame(
            data=list(zip(frequency, amplitude)),
            columns=["Frequency", "Intensity"]
        )
        self.fid_df = pd.DataFrame(
            data=list(zip(time * 1e6, proc_fid)),
            columns=["Time", "FID"]
        )

class FTBatch:
    """
        A general class for batch/surveys. The parent batch file dialog will
        pass the filepath to a batch file upon serialization, and the class
        parser method will then determine the settings and parameters used in
        the particular scan.

        Each scan is then loaded into memory as `scan` objects, and processed
        with the same filtering and window functions.

        This FTBatch object is intended to then be passed into the BatchViewerWindow
        which will then initialize a plot window for that particular scan.

        The peek argument is given as an option whether or not just to simply
        look at the settings contained in the batch file and not actually process
        the data.
    """
    def __init__(self, filepath=None, batch_type=None,
                 fidsettings=None, rootpath=None, peek=True):
        self.fidsettings = dict()

        self.settings = {
            "Root path": rootpath,
            "Date": None,
            "Scan number": 0,
            "Scan count": 0,
            "Start frequency": None,
            "End frequency": None,
            "Step size": None,
            "Cavity frequency": None,
            "Calibration count": 0,
            "Calibration": False,
            "Type": batch_type,                  # The batch file type
            "Scan list": list(),                 # List of scan numbers
            "Scan objects": dict(),              # Dictionary of scan objects
            "Calibration list": list(),          # List of calibration scans
            "Calibration objects": dict()        # Dictionary of calibration objects
        }
        if peek is False:
            if fidsettings is not None:
                # Take the FID processing settings
                self.fidsettings = {
                    key: None for key in ["exponential", "window function", "delay", "high pass", "low pass"]
                }
                self.build_dir_paths()
                self.fidsettings.update(fidsettings)
                self.convert_objects()

        if filepath is not None:
            # Open and parse the batch file
            settings, self.spectrum = parse_batch(filepath, peek)
            self.settings.update(settings)

    def build_dir_paths(self):
        # Build up the directory paths for all of the scans
        self.settings["Scan paths"] = dict()
        path = self.settings["Root path"] + "/scans/*/*/"
        for scan_id in self.settings["Scan list"]:
            self.settings["Scan paths"][scan_id] = glob(path + str(scan_id) + ".txt")[0]

    def stitch_spectra(self):
        """
            Class method for stitching a spectrum together from all of the
            individual scans.

            The way it works is via interpolation - each frequency window is
            interpolated into the same frequency bins, and the intensity is
            averaged across.

            The intensity outside of the original frequency range is set to NaN
            which allows me to take advantage of the fact that the final
            intensity does not take into account regions that have no measured
            intensity. There may be a better way of doing this...
        """
        if self.settings["Start frequency"] is not None:
            full_freq = np.arange(
                self.settings["Start frequency"],
                self.settings["End frequency"],
                self.settings["Step size"]
            )
            self.interpolants = list()
            for scan_id in self.settings["Scan objects"]:
                # Loop over all the scans and
                self.interpolants.append(
                    interp1d(
                        self.settings["Scan objects"][scan_id].spectrum["Frequency"],
                        self.settings["Scan objects"][scan_id].spectrum["Intensity"],
                        bounds_error=False,
                        fill_value=np.nan
                    )(full_freq)
                )
            intensity = np.nanmean(self.interpolants)
            np.nan_to_num(intensity, copy=False)
            self.spectrum["Frequency"] = full_freq
            self.spectrum["Intensity"] = intensity

    def convert_objects(self):
        # Class method for taking all of the scan IDs and subsequently serialize
        # all of them to FTData objects, processing them with the same settings
        for scan_id in self.settings["Scan list"]:
            if os.path.isfile(self.settings["Scan paths"][scan_id]) is False:
                pass
            else:
                instance = FTData(self.settings["Scan paths"][scan_id], fid=True)
                instance.fid2fft(
                    window_function = self.fidsettings["window function"],
                    delay = self.fidsettings["delay"],
                    band_pass=[self.fidsettings["high pass"], self.fidsettings["low pass"]],
                    exp_filter = self.fidsettings["exponential"],
                )
                self.settings["Scan objects"][scan_id] = instance
        if self.settings["Type"] == "surveys":
            self.stitch_spectra()

    def process_all_fids(self):
        # Class method for re-processing all of the FIDs without re-parsing
        self.spectrum = pd.DataFrame(columns=["Frequency", "Intensity"])
        for scan in self.settings["Scan objects"]:
            self.settings["Scan objects"][scan].fid2fft(
                window_function = self.fidsettings["window function"],
                delay = self.fidsettings["delay"],
                band_pass=[self.fidsettings["high pass"], self.fidsettings["low pass"]],
                exp_filter = self.fidsettings["exponential"],
            )
        # Generate the full spectrum
        if self.settings["Type"] == "surveys":
            self.stitch_spectra()

    """
        Double Resonance Class Methods

        These methods will be used for double resonance instances; first to
        preprocess the depletion spectra, then to fit them and report the
        fitted values back to the user.

    """

    def generate_depletion_spectrum(self, ranges=None):
        # Class method for generating the depletion spectrum using the
        # specified integration ranges.
        if ranges is not None:
            self.spectrum = None             # Reset the current spectrum
            spectra = dict()
            frequency = list()
            for index, int_range in enumerate(ranges):
                spectra[index] = list()
                for scan_id in self.settings["Scan objects"]:
                    dr_freq = self.settings["Scan objects"][scan_id].settings["DR frequency"]
                    if dr_freq not in frequency:
                        frequency.append(dr_freq)
                    spectra[index].append(
                        self.settings["Scan objects"][scan_id].spectrum.iloc[int_range]["Intensity"].sum()
                    )
            self.spectrum = pd.DataFrame.from_dict(
                spectra
            )
            self.spectrum["Frequencies"] = frequency

    def preprocess_dr(self, savgol=[0, 0]):
        # Class method for doing all of the cleaning before the DR spectra are
        # fit.
        # First up is coaveraging the columns
        intensity_cols = [key for key in list(self.spectrum.keys()) if key != "Frequency" and key != "Average"]
        self.spectrum["Average"] = self.spectrum[intensity_cols].mean(axis=1)
        if savgol == [0, 0]:
            pass
        else:
            try:
            # If your filter isn't being applied, you're using it wrong.
                self.spectrum["Average"] = spsig.savgol_filter(
                    self.spectrum["Average"],
                    savgol[0],
                    savgol[1]
                )
            except ValueError:
                pass

    def fit_dr(self, freq_range=None, savgol=[0, 0]):
        # First clean the DR
        self.preprocess_dr(savgol=savgol)
        # If we truncate the spectrum
        if freq_range is None:
            freq_range = [0., np.inf]
        truncated = self.spectrum.loc[(self.spectrum.Frequency >= min(freq_range)) & (self.spectrum["Frequency"] <= max(freq_range))]
        # First find the lowest point in depletion spectrum
        peak_guess = float(truncated.loc[truncated["Average"] == truncated["Average"].min()]["Frequency"])
        bounds = (
            [-np.inf, peak_guess - 1., 0.2, -np.inf],
            [0., peak_guess + 1., 10., np.inf]
        )
        p0 = [-1., peak_guess, 1., 0.]
        # Fit the truncated part of the spectrum
        popt, pcov = curve_fit(
            gaussian_func,
            truncated["Frequency"],
            truncated["Average"],
            p0=p0,
            bounds=bounds
        )
        # Generate the model Gaussian
        self.spectrum["Fit"] = gaussian_func(
            self.spectrum["Frequency"],
            *popt
        )
        self.fit_results = dict()
        # Errors as the sqrt of the diagonal of the covariance matrix
        errors = np.sqrt(np.diag(pcov))
        for param, opt, std in zip(["A", "Center", "Width", "Offset"], popt, errors):
            self.fit_results[param] = ufloat(opt, std)
