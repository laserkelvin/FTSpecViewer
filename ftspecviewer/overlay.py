
import pandas as pd

class Overlay:
    @classmethod
    def from_cat(cls, filepath):
        # Method to serialize an overlay instance from a cat file
        df = pd.readfwf(filepath, widths=[13,8,8,2,10,3,7,4,12,12], header=None)
        df.columns = ["Frequency", "Uncertainty", "Intensity", "DoF",
                      "Lower state energy", "Degeneracy", "ID", "Coding",
                      "Lower quantum numbers", "Upper quantum numbers"]
        # Extract filename
        name = filepath.split("/")[-1].split(".")[0]
        return Overlay(df, name)

    @classmethod
    def from_txt(cls, filepath):
        name = filepath.split("/")[-1].split(".")[0]
        with open(filepath, "r") as read_file:
            peek = read_file.readlines()[0]
            peek = peek.split()
            # Try and convert the first item in the first line to a float;
            # if it raises a ValueError it's most likely because the item is
            # actually a string. If that's the case, it's most likely a header!
            try:
                float(peek[0])
                skiprows = 0
            except ValueError:
            # The first line is a header, we need to skip it!
                skiprows = 1
        try:
            df = pd.read_csv(
                filepath,
                header=None,
                skiprows=skiprows,
                names=["Frequency", "Intensity"]
            )
            return Overlay(df, name)
        except ValueError:
            raise InvalidFormatting("Please provide two-column (frequency/intensity data)")

    def __init__(self, df, name, offset=None, norm=None):
        self.spectrum = df                    # Contains the data
        self.name = name                      # Identifier for overlay
        self.offset = offset                  # Vertical offset
        self.norm = norm                      # Normalization factor

    def refresh_spectrum(self):
        # This method will recalculate the overlay according to all of the settings
        if self.offset is not None:
            if len(self.offset) = 1:
                self.spectrum["Offset-Intensity"] = self.spectrum["Intensity"] + self.offset
            elif type(self.offset) is list and len(self.offset) = 2:
                # If a list if given with two values, shift the spectrum hor and vert
                self.spectrum["Offset-Frequency"] = self.spectrum["Frequency"] + self.offset[0]
                self.spectrum["Offset-Intensity"] = self.spectrum["Intensity"] + self.offset[1]
        if self.norm is not None:
            if "Offset-Intensity" in list(self.spectrum.keys()):
                self.norm_column = "Offset-Intensity"
            else:
                self.norm_column = "Intensity"
            if self.norm is True:
                # If no value is specified but a True value is passed, then
                # normalize to the largest value
                self.norm = self.spectrum[self.norm_column].max()
            # Perform the normalization
            self.spectrum["Normalized"] = self.spectrum[self.norm_column] / self.norm
