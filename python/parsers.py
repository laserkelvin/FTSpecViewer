import pandas as pd
import os

def parse_batch(filepath, peek=True):
    """ Generic parser for QtFTM batch files """
    # initialize some variables
    settings = {"Scan list": list(), "Calibration list": list()}
    comments = list()
    spectrum = list()
    read_spectrum = False
    read_scans = False
    read_calscans = False
    # Open file for reading
    with open(filepath, "r") as read_file:
        # General method for parsing details about a batch run
        # Continue statements are used because each line will have one and
        # only one condition satisfactory
        for line in read_file:
            if "#" in line:
                comments.append(line)
                continue
            if line == os.linesep:
                # If we encounter a blank line, stop reading everything
                read_spectrum = False
                read_scans = False
                read_calscans = False
                continue
            if read_scans is True:
                try:
                    settings["Scan list"].append(int(line))
                except ValueError:
                    pass
            if read_calscans is True:
                try:
                    settings["Calibration list"].append(int(line))
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
                settings["Cavity frequency"] = float(comment.split()[2])
            if "Start freq" in comment:
                settings["Start frequency"] = float(comment.split()[2])
            if "End freq" in comment:
                settings["End frequency"] = float(comment.split()[2])
            if "Step size" in comment:
                settings["Step size"] = float(comment.split()[2])
            if "Date" in comment:
                settings["Date"] = comment
        # Convert the parsed data into a pandas dataframe
        if peek is False:
            spectrum = np.array(spectrum)
            ncols = spectrum.shape[1] - 1       # Get number of columns
            columns = ["Frequency"] + ["Trace " + str(col) for col in range(ncols)]
            spectrum = pd.DataFrame(
                data=spectrum,
                columns=columns
            )
    return settings, spectrum

def parse_fid(filepath, mmw=False):
    """ Function to read in the settings in an FID from QtFTM """
    read_fid = False
    settings = dict()
    comments = list()
    gases = dict()
    timings = dict()
    fid = list()
    with open(filepath, "r") as read_file:
        if mmw is False:
            for line in read_file:
                if "#" in line:
                    comments.append(line)
                        # Settings lines are commented with "#"
                if read_fid is True:
                    fid.append(float(line))
                if "fid" in line:
                    # Start reading the FID in after this line is found
                    read_fid = True
            for comment in comments:
                split_comment = comment.split("#")[1].split()
                if "Scan" in comment:
                    # Read in the scan ID
                    settings["ID"] = "-".join(split_comment[1:])
                if "Date" in comment:
                    settings["Date"] = comment
                elif "Shots" in comment:
                    # Read in the number of Shots
                    settings["Shots"] = int(split_comment[1])
                elif "Cavity freq" in comment:
                    # Read in the cavity frequency; units of MHz
                    settings["Frequency"] = float(split_comment[2])
                elif "Tuning Voltage" in comment:
                    # Read in tuning voltage; units of mV
                    settings["Tuning voltage"] = int(split_comment[2])
                elif "Attenuation" in comment:
                    # Read in the Attenuation; units of dB
                    settings["Attenuation"] = int(split_comment[1])
                elif "Cavity Voltage" in comment:
                    # Read in cavity voltage; units of mV
                    settings["Cavity voltage"] = int(split_comment[2])
                elif "FID spacing" in comment:
                    # Read in the FID spacing, units of seconds
                    settings["FID spacing"] = float(split_comment[2])
                elif "FID points" in comment:
                    # Read in the number of points we expect for the FID
                    settings["FID points"] = int(split_comment[2])
                elif "Probe" in comment:
                    # The probe frequency, in MHz
                    settings["Probe frequency"] = float(split_comment[2])
                elif "DR freq" in comment:
                    # Double resonance frequency in MHz
                    settings["DR frequency"] = float(split_comment[2])
                elif "DR power" in comment:
                    settings["DR power"] = int(split_comment[2])
                elif "Pressure" in comment:
                    settings["Pressure"] = float(split_comment[1])
                elif "Rep rate" in comment:
                    settings["Rep rate"] = int(split_comment[2])
                elif "Magnet" in comment:
                    settings["Magnet"] = int(split_comment[2]) != 0
        elif mmw is True:
            read_params = False
            read_int = False
            for line in read_file:
                if "SURVEY" in line:
                    scan_details = line.split()
                    settings["ID"] = int(scan_details[1])
                    settings["Date"] = str(scan_details[4])
                    read_params = True
                    read_int = False
                    intensities = list()
                    continue
                if read_params is True:
                    # Read in the frequency step, frequency, and other info
                    # needed to reconstruct the frequency data
                    scan_params = read_file[1].split()
                    shift = 1
                    settings["Frequency"] = float(scan_params[0])
                    settings["Frequency step"] = float(scan_params[1])
                    if len(scan_params) == 4:
                        settings["Multiplier"] = 1
                        shift = 0
                    # If the multiplier data is there, we don't shift the read
                    # index over by one
                    else:
                        settings["Multiplier"] = int(scan_params[2])
                    settings["Center"] = float(scan_params[2 + i])
                    settings["Points"] = int(scan_params[3 + i])
                    read_params = False
                    # Start reading intensities immediately afterwards
                    read_int = True
                    continue
                if read_int is True:
                    intensities += line.split()
    return settings, fid
