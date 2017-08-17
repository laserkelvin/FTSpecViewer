import numpy as np
import pandas as pd
from scipy import signal as spsig
import peakutils

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

    def fid2fft(self, window_function=None, dc_offset=True, exp_filter=None, delay=None):
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
    """
    def __init__(self, filepath=None, fidsettings=None):
        self.fidsettings = dict()

        self.settings = {
            "Date": None,
            "Scan number": 0,
            "Scan count": 0,
            "Step size": 0.,
            "Calibration count": 0,
            "Calibration": False,
            "Type": None,                        # The batch file type
            "Scan list": list(),                 # List of scan numbers
            "Scan objects": dict(),              # Dictionary of scan objects
            "Calibration list": list(),          # List of calibration scans
            "Calibration objects": dict()        # Dictionary of calibration objects
        }
        if fidsettings is not None:
            # Take the FID processing settings
            self.fidsettings.update(fidsettings)

        if filepath is not None:
            # Open and parse the batch file
            self.parse_batch(filepath)

    def parse_batch(self, filepath):
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
                if read_spectrum is True:
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
            # Convert the parsed data into a pandas dataframe
            self.spectrum = pd.DataFrame(
                data=spectrum,
                #columns=["Frequency"] + ["Intensity" + str(index) for index in range(1,len(spectrum[0]))]
            )

    def convert_objects(self, root_path, object_class):
        """ Method for converting all of the scan numbers into scan objects """
        return None
