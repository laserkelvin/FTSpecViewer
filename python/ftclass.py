import numpy as np
import pandas as pd
from scipy import signal as spsig
import peakutils

class FTData:
    """ A general class for processing FTMW and FTCP data.
        A file is specified, with the argument `fid` that will determine
        whether or not the data being loaded is an FID, or a tab delimited
        frequency/intensity spectrum.
    """
    def __init__(self, filepath=None, fid=False):
        self.settings = dict()
        if fid is True:
            self.fid = list()
            with open(filepath, "r") as fid_file:
                self.parsed_data = fid_file.readlines()
            self.read_fid_settings()
            self.fid = np.array(self.fid)
        else:
            self.spectrum = pd.read_csv(
                filepath,
                delimiter="\t",
                skiprows=1,
                names=["Frequency", "Intensity"]
            )

    def read_fid_settings(self):
        """ Function to read in the settings in an FID from QtFTM """
        read_fid = False
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
                    elif "Attenunation" in line:
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

    def fid2fft(self, window_function=None, dc_offset=True, exp_filter=None):
        """ Perform the DFT of an FID using NumPy's FFT package. """
        available_windows = [
            "blackmanharris",
            "blackman",
            "boxcar",
            "gaussian",
            "hanning",
            "bartlett"
        ]
        if window_function is not None:
        # Use a scipy.signal window function to process the FID signal
            if window_function not in available_windows:
                print("Incorrect choice for window function.")
                print("Available:")
                print(available_windows)
            else:
                self.fid *= spsig.get_window(window_function, self.fid.size)
        # Perform the FFT
        if exp_filter is not None:
            self.fid *= spsig.exponential(self.fid.size, exp_filter)
        amplitude = np.fft.fft(self.fid)
        # Calclate the frequency window
        frequency = np.linspace(
            self.settings["Probe frequency"],
            self.settings["Probe frequency"] + 1.,
            amplitude.size
        )
        print(frequency.size, amplitude.size)
        self.spectrum = pd.DataFrame(
            data=list(zip(frequency, amplitude)),
            columns=["Frequency", "Intensity"]
        )