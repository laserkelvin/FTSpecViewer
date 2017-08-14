"""
A dedicated batch viewer class. This class is called by the main window when
a specific batch/survey is selected via the ScanChooserWindow.
"""
import sys
import os
import pandas as pd
import numpy as np
import yaml
from uncertainties import ufloat, unumpy
import pyqtgraph
from glob import glob

from ftclass import FTData
import fittingroutines as fr

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, qApp, QTableWidgetItem

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.data = None
        self.peaks = None
        self.peaks_df = None

        self.setupUi(self)
