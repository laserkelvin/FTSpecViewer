import numpy as np
import pandas as pd
from scipy import signal as spsig
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from uncertainties import ufloat, unumpy
import peakutils

from utils import FTDateTime
from fittingroutines import gaussian_func
from filters import *


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
            self.fid = list()
            with open(filepath, "r") as fid_file:
                self.parsed_data = fid_file.readlines()
            self.read_fid_settings()
            self.fid = np.array(self.fid)
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

    def read_fid_settings(self, mmw=False):
        """ Function to read in the settings in an FID from QtFTM """
        read_fid = False
        if mmw is False:
            for line in self.parsed_data:
                split_line = line.split()
                if len(split_line) != 0:
                    if "#" in split_line[0]:
                        # Settings lines are commented with "#"
                        if "Scan" in line:
                            # Read in the scan ID
                            self.settings["ID"] = "-".join(split_line[1:])
                        elif "Shots" in line:
                            # Read in the number of Shots
                            self.settings["Shots"] = int(split_line[1])
                        elif "Cavity freq" in line:
                            # Read in the cavity frequency; units of MHz
                            self.settings["Frequency"] = float(split_line[2])
                        elif "Tuning Voltage" in line:
                            # Read in tuning voltage; units of mV
                            self.settings["Tuning voltage"] = int(split_line[2])
                        elif "Attenuation" in line:
                            # Read in the Attenuation; units of dB
                            self.settings["Attenuation"] = int(split_line[1])
                        elif "Cavity Voltage" in line:
                            # Read in cavity voltage; units of mV
                            self.settings["Cavity voltage"] = int(split_line[2])
                        elif "FID spacing" in line:
                            # Read in the FID spacing, units of seconds
                            self.settings["FID spacing"] = float(split_line[2])
                        elif "FID points" in line:
                            # Read in the number of points we expect for the FID
                            self.settings["FID points"] = int(split_line[2])
                        elif "Probe" in line:
                            # The probe frequency, in MHz
                            self.settings["Probe frequency"] = float(split_line[2])
                    if read_fid is True:
                        self.fid.append(float(line))
                    if "fid" in line:
                        # Start reading the FID in after this line is found
                        read_fid = True
        elif mmw is True:
            read_params = False
            read_int = False
            for line in self.parsed_data:
                if "SURVEY" in line:
                    scan_details = line.split()
                    self.settings["ID"] = int(scan_details[1])
                    self.settings["Date"] = str(scan_details[4])
                    read_params = True
                    read_int = False
                    intensities = list()
                    continue
                if read_params is True:
                    # Read in the frequency step, frequency, and other info
                    # needed to reconstruct the frequency data
                    scan_params = self.parsed_data[1].split()
                    shift = 1
                    self.settings["Frequency"] = float(scan_params[0])
                    self.settings["Frequency step"] = float(scan_params[1])
                    if len(scan_params) == 4:
                        self.settings["Multiplier"] = 1
                        shift = 0
                    # If the multiplier data is there, we don't shift the read
                    # index over by one
                    else:
                        self.settings["Multiplier"] = int(scan_params[2])
                    self.settings["Center"] = float(scan_params[2 + i])
                    self.settings["Points"] = int(scan_params[3 + i])
                    read_params = False
                    # Start reading intensities immediately afterwards
                    read_int = True
                    continue
                if read_int is True:
                    intensities += line.split()

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
            proc_fid = apply_butter_filter(
                proc_fid,
                band_pass[0],
                band_pass[1],
                1. / self.settings["FID spacing"]
            )
        # Set the FID time points to zero
        if delay is not None:
            for index in range(delay):
                proc_fid[index] = 0.
        # Use a scipy.signal window function to process the FID signal
        if window_function is not None:
            if window_function not in available_windows:
                print("Incorrect choice for window function.")
                print("Available:")
                print(available_windows)
            else:
                proc_fid *= spsig.get_window(window_function, proc_fid.size)
        # Apply the exponential filter to smooth
        if exp_filter is not None:
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
        self.root_path = rootpath

        self.settings = {
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
                self.fidsettings = {key: None for key in ["exponential", "window function", "delay", "high pass", "low pass"]}
                self.fidsettings.update(fidsettings)
                self.convert_objects()

        if filepath is not None:
            # Open and parse the batch file
            self.parse_batch(filepath, peek)

#            if len(list(fidsettings.keys())) != 0:
                # If the FID config was changed, reload and reprocess all the FIDs
#                self.convert_objects()

    def parse_batch(self, filepath, peek=True):
        """ Generic parser for QtFTM batch files """
        comments = list()
        spectrum = list()
        read_spectrum = False
        read_scans = False
        read_calscans = False
        with open(filepath, "r") as read_file:
            # General method for parsing details about a batch run
            # Continue statements are used because each line will have one and
            # only one condition satisfactory
            for line in read_file:
                if "#" in line:
                    comments.append(line)
                    continue
                if line == "\n":
                    # If we encounter a blank line, stop reading everything
                    read_spectrum = False
                    read_scans = False
                    read_calscans = False
                    continue
                if read_scans is True:
                    try:
                        self.settings["Scan list"].append(int(line))
                    except ValueError:
                        pass
                if read_calscans is True:
                    try:
                        self.settings["Calibration list"].append(int(line))
                    except ValueError:
                        pass
                if read_spectrum is True and peek is False:
                    # Start reading the spectrum in
                    try:
                        split_line = line.split()
                        values = [float(value) for value in split_line]
                        #print(values)
                        spectrum.append(values)
                    except ValueError:
                        pass
                if "surveyfreq" in line or "drfreq" in line:
                    # Detect that the frequency spectrum has begun
                    read_spectrum = True
                if "surveyscans" in line or "drscans" in line:
                    # Flag the scan number reading
                    read_scans = True
                if "surveycal" in line or "drcal" in line:
                    # Flag the calibration scan numbers to be read
                    read_calscans = True
            for comment in comments:
                if "FT freq" in comment:
                    self.settings["Cavity frequency"] = float(comment.split()[2])
                if "Start freq" in comment:
                    self.settings["Start frequency"] = float(comment.split()[2])
                if "End freq" in comment:
                    self.settings["End frequency"] = float(comment.split()[2])
                if "Step size" in comment:
                    self.settings["Step size"] = float(comment.split()[2])
                if "Date" in comment:
                    self.settings["Date"] = FTDateTime(comment)
            # Convert the parsed data into a pandas dataframe
            if peek is False:
                spectrum = np.array(spectrum)
                ncols = spectrum.shape[1] - 1       # Get number of columns
                columns = ["Frequency"] + ["Trace " + str(col) for col in range(ncols)]
                self.spectrum = pd.DataFrame(
                    data=spectrum,
                    columns=columns
                )

    def build_dir_paths(self):
        # Build up the directory paths for all of the scans
        self.settings["Scan paths"] = dict()
        for scan_id in self.settings["Scan list"]:
            self.settings[scan_id] = self.root_path + "/" + self.batch_type + "/*/" + str(scan_id) + ".txt"

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
        self.spectrum = pd.DataFrame(columns=["Frequency", "Intensity"])
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
                self.spectrum = self.spectrum.append(instance.spectrum, ignore_index=True)
                self.settings["Scan objects"][scan_id] = instance

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
        self.stitch_spectra()

    """
        Double Resonance Class Methods

        These methods will be used for double resonance instances; first to
        preprocess the depletion spectra, then to fit them and report the
        fitted values back to the user.

    """

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
        errors = np.sqrt(np.diag(pcov))
        for param, opt, std in zip(["A", "Center", "Width", "Offset"], popt, errors):
            self.fit_results[param] = ufloat(opt, std)
