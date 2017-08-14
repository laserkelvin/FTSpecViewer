import sys
import os
import pandas as pd
import numpy as np
import yaml
from uncertainties import ufloat, unumpy
import pyqtgraph

from ftclass import FTData
import fittingroutines as fr

# Qt related modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, qApp, QTableWidgetItem
from qtmain import Ui_MainWindow
from qtsettings import Ui_SettingsForm
from qtchooser import Ui_ScanChooser

################# Main Window #################

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.data = None
        self.peaks = None
        self.peaks_df = None

        self.setupUi(self)
        self.settings_dialog = SettingsWindow(self)         # Settings Window

        self.menubar.setNativeMenuBar(False)
        self.link_ui_actions()
        self.initialize_plot()

    def link_ui_actions(self):
        """ Method for consolidating all of the signal events in the UI
            If new objects are added to the GUI, make sure to add the connection
            to this function.
        """
        # File I/O actions
        self.actionSpectrum.triggered.connect(self.load_spectrum)
        self.actionFID.triggered.connect(self.load_FID)
        self.actionSave_spectrum.triggered.connect(self.save_spectrum)
        self.actionSave_FID.triggered.connect(self.save_fid)
        self.actionSave_peaks.triggered.connect(self.save_peaks)

        # Top level program interactions
        self.actionSettings.triggered.connect(self.open_settings)
        self.actionExit.triggered.connect(qApp.quit)

        # Processing the FIDs
        self.comboBoxWindowFunction.currentTextChanged.connect(self.process_fid)
        self.spinBoxExpFilter.valueChanged.connect(self.process_fid)
        self.spinBoxDelay.valueChanged.connect(self.process_fid)
        self.actionFit_Gaussian.triggered.connect(self.fit_fft)

        # Peak detection routines
        self.checkBoxDetectPeaks.stateChanged.connect(self.peak_detection_bool_update)
        self.doubleSpinBoxPeakSNRThres.valueChanged.connect(self.detect_peaks)
        self.doubleSpinBoxPeakMinDist.valueChanged.connect(self.detect_peaks)

    def peak_detection_bool_update(self):
        # Toggles on and off
        self.detect_peaks_bool = not self.detect_peaks_bool
        self.detect_peaks()

    def detect_peaks(self):
        # Peak detection signal event. If the checkbox for peak detection is
        # ticked, then peak detection will take place.
        # The peak frequencies will be searched, and reflected in the main plot
        # and peak table
        if self.detect_peaks_bool is True:
            self.peaks = 0                               # Reset the peak data
            self.statusBar.showMessage("Finding peaks...")
            peak_freqs, peak_intensities = fr.find_peaks(
                self.data.spectrum["Frequency"],
                self.data.spectrum["Intensity"],
                thres=float(self.doubleSpinBoxPeakSNRThres.value()),
                min_dist=float(self.doubleSpinBoxPeakMinDist.value())
            )
            self.peaks = list(zip(peak_freqs, peak_intensities))
            self.peaks_df = pd.DataFrame(
                data=self.peaks,
                columns=["Frequency", "Intensity"]
            )
            self.update_peak_table()
            self.update_plot()

    def update_peak_table(self):
        # Method for updating the peak table widget
        self.tableWidgetPeakTable.clear()
        # Set the number of rows
        self.tableWidgetPeakTable.setRowCount(len(self.peaks))
        # Set two columns
        self.tableWidgetPeakTable.setColumnCount(2)
        # Set the column headers
        for index, header in enumerate(["Frequency", "Intensity"]):
            self.tableWidgetPeakTable.setHorizontalHeaderItem(index, QTableWidgetItem(header))
        # Loop over all peaks, and populate the table
        for peak_num, peak in enumerate(self.peaks):
            self.tableWidgetPeakTable.insertRow(peak_num)
            for index, value in enumerate(peak):
                self.tableWidgetPeakTable.setItem(peak_num, index, QTableWidgetItem("{:.4f}".format(value)))

    def process_fid(self):
        # This routine is only run if a FID has been loaded
        # Basically it will process the FID and update the plots on the fly
        if self.fid is True:
            exp_filter = float(self.spinBoxExpFilter.value())
            window = str(self.comboBoxWindowFunction.currentText())
            delay = int(self.spinBoxDelay.value())

            if window == "none":
                window = None
            if exp_filter <= 0:
                exp_filter = None
            if delay <= 0:
                delay = None
            self.data.fid2fft(
                window_function=window,
                exp_filter=exp_filter,
                delay=delay
            )
            self.update_plot()

    def initialize_plot(self):
        # Method that will set up the PlotWidget settings
        self.graphicsViewMain.setBackground(None)
        self.graphicsViewFID.setBackground(None)
        self.graphicsViewMain.setAspectLocked(False)
        self.graphicsViewFID.setAspectLocked(False)
        #self.graphicsViewMain.addLegend()

        # Antialiased plots
        pyqtgraph.setConfigOption("antialias", True)
        pyqtgraph.setConfigOption("foreground", (7,136,155))

        for axis, label in zip(["bottom", "left"], ["Frequency (MHz)", "Intensity"]):
            self.graphicsViewMain.getAxis(axis).setLabel(label)
            self.graphicsViewMain.getAxis(axis).setPen((7,136,155))

        for axis, label in zip(["bottom", "left"], ["Time (us)", "FID"]):
            self.graphicsViewFID.getAxis(axis).setLabel(label)
            self.graphicsViewFID.getAxis(axis).setPen((7,136,155))

    def update_plot(self):
        # Method to plot the current spectrum
        self.graphicsViewMain.clear()
        self.graphicsViewFID.clear()
        self.graphicsViewMain.setAspectLocked(False)
        self.graphicsViewFID.setAspectLocked(False)
        self.graphicsViewMain.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Intensity"].astype(float),
                pen=(7,136,155),
                name="Spectrum"
            )
        # Plot the fitted data
        if "Fit" in list(self.data.spectrum.keys()):
            self.graphicsViewMain.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Fit"].astype(float),
                pen=(227,114,34),
                name="Fit"
            )
        # Plot the peak locations
        if self.peaks_df is not None and self.detect_peaks_bool is True:
            peak_plot = pyqtgraph.ScatterPlotItem(
                x=self.peaks_df["Frequency"].astype(float),
                y=self.peaks_df["Intensity"].astype(float),
                pen=(238,170,123),
                name="Peaks"
            )
            self.graphicsViewMain.addItem(peak_plot)
            self.statusBar.showMessage("Plotting the peaks...")
        # If we're looking at FID data
        if self.fid is True:
            self.graphicsViewFID.clear()
            self.graphicsViewFID.plot(
                self.data.fid_df["Time"].astype(float),
                self.data.fid_df["FID"].astype(float),
                pen=(7,136,155),
                name="FID"
            )

    def save_spectrum(self):
        if self.data:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.data.spectrum.to_csv(filepath)

    def save_fid(self):
        # Method for exporting a FID via Pandas dataframe method
        if self.fid is True:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.data.fid.to_csv(filepath)

    def save_peaks(self):
        # Method for exporting the detected peaks via Pandas dataframe method
        if self.peaks_df is not None:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.peaks.to_csv(filepath)

    def fit_fft(self):
        # Function to perform an automatic fit to the FFT spectrum
        if self.fid is True:
            peakfreq, peakint = fr.find_peaks(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Intensity"].astype(float)
            )
            if len(peakfreq) < 2 or len(peakfreq) % 2 == 0 is False:
                # Make sure number of detected peaks is even, and more than two.
                peakfreq = None
            # Call the fitting function
            try:
                popt, pcov = fr.fit_lineshape(
                    fr.arb_gaussian_func,
                    self.data.spectrum["Frequency"].astype(float),
                    self.data.spectrum["Intensity"].astype(float),
                    peakfreq
                )
                self.data.spectrum["Fit"] = fr.arb_gaussian_func(
                    self.data.spectrum["Frequency"].astype(float),
                    *popt
                )
                # Package the fitted parameters, and their uncertainties
                # Calculate the center frequency
                center_freq = np.average([popt[1] + popt[4]])
                self.labelCenterFrequency.setText(str(round(center_freq, 4)))
                self.update_plot()

            except RuntimeError:
                self.statusBar.showMessage("Fit not converged.")

    def format_uncertainty(self, ufloat_type):
        # This function will be used enough to format the uncertainty output
        return "{:.3uS}".format(ufloat_type)

    def load_spectrum(self):
        # Method to load a general spectrum, with tab delimited
        # frequency and intensity columns
        filepath = QFileDialog.getOpenFileName(self, "Open a spectrum file")

        try:
            self.initialize_plot()
            self.statusBar.showMessage("Loading spectrum...")
            self.data = FTData(filepath[0], fid=False)
            self.fid = False
            # Straight plot without fuss
            self.statusBar.showMessage("Displaying plot.")
            self.update_plot()
        except FileNotFoundError:
            self.statusBar.showMessage("File not found!")

    def load_FID(self):
        # Method to load an FID from file
        filepath = QFileDialog.getOpenFileName(self, "Open a FID file")

        try:
            self.initialize_plot()
            self.statusBar.showMessage("Loading FID...")
            self.data = FTData(filepath[0], fid=True)
            if self.data.fid.size > 10:
                # This case checks to see if there IS an FID loaded; if not,
                # give up on doing anymore analysis to prevent crashing
                self.fid = True
                # Perform initial FFT
                self.statusBar.showMessage("Performing FFT...")
                self.data.fid2fft()
                # Plot the data
                self.statusBar.showMessage("Displaying plot.")
                self.update_plot()
                # Update the scan details
                self.labelTuning.setText(str(self.data.settings["Tuning voltage"]))
                self.labelScanNum.setText(str(self.data.settings["ID"]))
                self.labelShotCount.setText(str(self.data.settings["Shots"]))
                self.labelAttenuation.setText(str(self.data.settings["Attenuation"]))
            else:
                self.statusBar.showMessage("Error loading FID!")

        except FileNotFoundError:
            self.statusBar.showMessage("File not found!")

    def open_settings(self):
        # Show the settings dialog
        self.settings_dialog.show()


################# Settings Window Dialog #################

class SettingsWindow(QMainWindow, Ui_SettingsForm):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)

        self.config = dict()

        self.setupUi(self)
        self.init_actions()
        self.read_settings()

    def init_actions(self):
        # Method for connecting signals to events
        # Save and close buttons
        self.pushButtonCloseSettings.clicked.connect(self.close_dialog)
        self.pushButtonSaveSettings.clicked.connect(self.write_settings)

        self.commandLinkButtonQTFTMPath.clicked.connect(self.browse_qtftm)

    def read_settings(self):
        # Read in the settings from the config.yaml file in the same directory
        if os.path.isfile("config.yaml") is False:
            with open("config.yaml", "w+") as write_file:
                write_file.write("# Automatically generated config.yaml for FTSpecViewer")
        with open("config.yaml", "r") as read_file:
            self.config = yaml.safe_load(read_file)
        try:
            self.lineEditChirpPath.setText(self.config["paths"]["chirp_path"])
            self.lineEditQtFTMPath.setText(self.config["paths"]["qtftm_path"])
        except KeyError:
            pass

    def browse_qtftm(self):
        # Open a file dialog to navigate to the QtFTM folder
        folderpath = QFileDialog.getExistingDirectory(self, "Navigate to QtFTM root folder")

        if folderpath:
            self.config["paths"]["qtftm_path"] = folderpath
            self.lineEditQtFTMPath.setText(folderpath)

    def browse_chirp(self):
        # Open a file dialog to navigate to the blackchirp folder
        folderpath = QFileDialog.getExistingDirectory(self, "Navigate to QtFTM root folder")

        if folderpath:
            self.config["paths"]["chirp_path"] = folderpath
            self.lineEditChirpPath.setText(folderpath)

    def write_settings(self):
        # Update the settings first
        self.config["paths"]["chirp_path"] = self.lineEditChirpPath.text()
        self.config["paths"]["qtftm_path"] = self.lineEditQtFTMPath.text()
        with open("config.yaml", "w+") as write_file:
            yaml.safe_dump(
                self.config,
                write_file
            )

    def close_dialog(self):
        # Shut down the settings dialog
        self.close()

################# Settings Window Dialog #################

class ScanChooserWindow(QMainWindow, Ui_ScanChooser):
    def __init__(self, parent=None, root_path=None):
        super(ScanChooserWindow, self).__init__(parent)

        self.config = dict()
        self.active_control = None
        self.root_path = root_path
        self.dir = {"dr": list(), "survey": list(), "batch": list()}

        self.setupUi(self)
        self.init_actions()
        self.read_latest()

    def init_actions(self):
        self.pushButtonCloseChooser.clicked.connect(self.close_dialog)
        self.comboBoxScanChooser.currentTextChanged.connect(self.update_scan_table)
        self.tableWidgetScanChooser.currentItemChanged.connect(self.select_scan)

    def select_scan(self):
        scan_number = int(self.tableWidgetScanChooser.currentItem())
        self.spinBoxBatchNumber.setValue(scan_number)

    def read_latest(self):
        # Method for finding out what the most recent scan is for each Batch
        if self.root_path is not None and os.path.isdir(self.root_path) is True:
            for batch_type in ["dr", "survey", "batch"]:
                subdir = os.path.join(self.root_path, batch_type)
                self.dir[batch_type] = glob(
                    subdir + "/*/*.txt"
                )

    def update_scan_table(self):
        # Method for updating the scan table, depending on the choice of batch
        # type.
        self.tableWidgetScanChooser.clear()
        choice = str(self.comboBoxScanChooser.currentText()).lower()
        self.tableWidgetScanChooser.setRowCount(len(self.dir[choice]))
        self.tableWidgetScanChooser.setColumnCount(1)

        for index, file in enumerate(self.dir[choice]):
            filename = file.split("/")[-1]      # Get the filename with extension
            filename = filename.split(".")[0]   # Strip extension
            self.tableWidgetScanChooser.insertRow(index)
            self.tableWidgetScanChooser.setItem(index, 0, filename)

    def close_dialog(self):
        self.close()
