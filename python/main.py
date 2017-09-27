import sys
import os
import pandas as pd
import numpy as np
import yaml
from uncertainties import ufloat, unumpy
import pyqtgraph
from glob import glob

from ftclass import FTData, FTBatch
import fittingroutines as fr
from utils import CreateDatabase, CompressData, AddDatabaseEntry

# Qt related modules
from PyQt5.QtWidgets import (QMainWindow, QFileDialog,
                             QApplication, qApp, QTableWidgetItem)
from PyQt5.QtCore import QDate
from batchviewer import BatchViewerWindow
from qtmain import Ui_MainWindow
from qtsettings import Ui_SettingsForm
from qtchooser import Ui_ScanChooser
from fonts_rc import *
from icons_rc import *

################# Main Window #################


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.pick_peaks = False
        self.doppler_count = 0
        self.doppler_param = dict()
        self.data = None
        self.peaks = None
        self.peaks_df = None

        self.setupUi(self)
        self.settings_dialog = SettingsWindow(self)         # Settings Window
        self.batch_dialog = ScanChooserWindow(
            self, self.settings_dialog.config["paths"]["qtftm_path"]
        )         # Batch dialog

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
        self.actionFTB.triggered.connect(self.export_ftb)
        self.actionStick_spectrum.triggered.connect(self.export_sticks)

        # Top level program interactions
        self.actionSettings.triggered.connect(self.open_settings)
        self.actionBatch.triggered.connect(self.open_batch)
        self.actionExit.triggered.connect(qApp.quit)

        # Processing the FIDs
        self.comboBoxWindowFunction.currentTextChanged.connect(self.process_fid)
        self.spinBoxExpFilter.valueChanged.connect(self.process_fid)
        self.spinBoxHighPass.valueChanged.connect(self.process_fid)
        self.spinBoxLowPass.valueChanged.connect(self.process_fid)
        self.spinBoxDelay.valueChanged.connect(self.process_fid)
        self.actionFit_Gaussian.triggered.connect(self.fit_fft)

        # Peak detection routines
        self.checkBoxDetectPeaks.stateChanged.connect(self.peak_detection_bool_update)
        self.doubleSpinBoxPeakSNRThres.valueChanged.connect(self.detect_peaks)
        self.doubleSpinBoxPeakMinDist.valueChanged.connect(self.detect_peaks)
        self.pushButtonAutofit.clicked.connect(self.auto_doppler)

        # Peak picking routine
        if self.pick_peaks is True:
            self.doppler_count = 0
            self.graphcsViewMain.scene().sigMouseClicked.connect(self.manual_doppler_fit)

    def peak_detection_bool_update(self):
        # Toggles on and off
        self.detect_peaks_bool = not self.detect_peaks_bool
        self.detect_peaks()

    def pick_peaks_bool_update(self):
        # Toggles peak picking on and off
        self.pick_peaks = not self.pick_peaks

    def manual_doppler_fit(self):
        self.doppler_count = 0
        self.graphicsViewMain.scene()

    def auto_doppler(self):
        # Detect peaks Automatically
        self.doppler_sets = list()
        # Perform peak detection to do a quick search for frequencies
        self.detect_peaks_bool = True
        self.detect_peaks()
        self.detect_peaks_bool = False
        while (len(self.peaks) / 2.) >= 1:
            pair = list()
            for i in range(2):
                pair.append(self.peaks.pop())
            self.doppler_sets.append(pair)
        self.peaks = list()
        self.peaks_df.drop(self.peaks_df.index, inplace=True)
        for index, pair in enumerate(self.doppler_sets):
            frequencies = [pair[0][0], pair[1][0]]
            intensity = np.average([pair[0][1], pair[1][1]])
            self.doppler_param[index] = fr.fit_doppler_pair(self.data.spectrum, frequencies)
            self.peaks_df = self.peaks_df.append(
                {"Frequency": self.doppler_param[index]["Frequency"].n,
                 "Intensity": intensity},
                ignore_index=True
            )
            self.peaks.append([self.doppler_param[index]["Frequency"].n, intensity])
        self.update_peak_table()
        self.update_plot()
        print(self.peaks_df)

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
            high_pass = float(self.spinBoxHighPass.value())
            low_pass = float(self.spinBoxLowPass.value())

            if window == "none":
                window = None
            if exp_filter <= 0:
                exp_filter = None
            band_pass = None
            if high_pass != 0. or low_pass != 0.:
                band_pass = [low_pass, high_pass]
            if delay <= 0:
                delay = None
            self.data.fid2fft(
                window_function=window,
                band_pass=band_pass,
                exp_filter=exp_filter,
                delay=delay
            )
            self.update_plot()

    def export_sticks(self):
        """ Function to export a stick spectrum """
        try:
            intensities = np.zeros(len(self.data.spectrum["Frequency"]))
            self.stick_spectrum = pd.DataFrame(
                list(zip(self.data.spectrum["Frequency"].astype(float), intensities)),
                columns=["Frequency", "Intensity"]
            )
            self.stick_spectrum = pd.concat([self.stick_spectrum, self.peaks_df])
            self.stick_spectrum.sort_values(["Frequency"], ascending=True, inplace=True)
            filepath = QFileDialog.getSaveFileName(self, "Save the stick spectrum")
            if len(filepath[0]) > 1:
                self.stick_spectrum.to_csv(filepath[0], index=False)
        except NameError:
            self.statusBar.showMessage("No sticks to spectrum!")

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
                self.data.spectrum.to_csv(filepath[0], index=False)

    def save_fid(self):
        # Method for exporting a FID via Pandas dataframe method
        if self.fid is True:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.data.fid.to_csv(filepath[0], index=False)

    def save_peaks(self):
        # Method for exporting the detected peaks via Pandas dataframe method
        if self.peaks_df is not None:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.peaks_df.to_csv(filepath[0])

    def export_ftb(self):
        if self.peaks_df is not None:
            filepath = QFileDialog.getSaveFileName(self, "Export peaks to FTB file.")
            self.peaks_df.sort_values(["Intensity"], ascending=False, inplace=True)
            if filepath:
                freq = self.peaks_df["Frequency"].astype(float)
                # normalize the intensities
                intensities = self.peaks_df["Intensity"].astype(float) / self.peaks_df["Intensity"].max()
                # Number of shots for strongest line is 10 shots
                shots = [10. / (value**2.) for value in intensities]
                merged = np.column_stack((freq, shots))
                np.savetxt(
                    fname=str(filepath[0]),
                    X=merged,
                    fmt=("ftm:%5.3f", " shots:%4i")
                )

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

    def open_batch(self):
        self.batch_dialog.show()


################# Settings Window Dialog #################

class SettingsWindow(QMainWindow, Ui_SettingsForm):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)

        self.config = {
            "paths": {
                "qtftm_path": None,
                "chirp_path": None
            }
        }

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
    def __init__(self, parent=None, qtftm_root=None):
        super(ScanChooserWindow, self).__init__(parent)

        self.config = dict()
        self.filter = False
        self.active_control = None
        self.root_path = qtftm_root
        self.dir = {"dr": list(), "surveys": list(), "batch": list()}
        self.batch_objects = {"dr": dict(), "surveys": dict(), "batch": dict()}

        self.setupUi(self)
        self.init_actions()
        self.configure_calendar_range()
        self.read_latest()
        self.update_scan_table()

    def init_actions(self):
        self.pushButtonCloseChooser.clicked.connect(self.close_dialog)
        self.pushButtonOpenScan.clicked.connect(self.create_batch_object)
        self.comboBoxScanChooser.currentTextChanged.connect(self.update_scan_table)
        self.tableWidgetScanChooser.currentItemChanged.connect(self.select_scan)
        # FID processing config
        self.comboBoxWindowFunction.currentTextChanged.connect(self.update_config)
        self.spinBoxDelay.valueChanged.connect(self.update_config)
        self.spinBoxHighPass.valueChanged.connect(self.update_config)
        self.spinBoxExpFilter.valueChanged.connect(self.update_config)
        # Calendar updating
        self.calendarWidgetEndDate.clicked.connect(self.configure_calendar_range)
        self.calendarWidgetStartDate.clicked.connect(self.configure_calendar_range)
        # Filter updating
        self.checkBoxFilter.stateChanged.connect(self.toggle_filter_bool)
        # Caching
        self.toolButtonCacheData.clicked.connect(self.compress_data)

    def configure_calendar_range(self, move_dates=False):
        # Initialize the calendars so that dates that can be selected are
        # sensible
        # Programmatically change the default date to some early time
        #if move_dates is True:
        self.calendarWidgetStartDate.setSelectedDate(QDate(2010, 1, 1))
        self.calendarWidgetEndDate.setSelectedDate(QDate.currentDate())
        # The End Date Calendar range depends on the Start Date - you can't
        # select an end date before the start.
        self.calendarWidgetEndDate.setDateRange(
            self.calendarWidgetStartDate.selectedDate(),
            QDate.currentDate()
        )
        # Conversely, you can't pick a starting date after the End Date
        self.calendarWidgetStartDate.setDateRange(
            QDate.fromString("2010-01-01"),
            self.calendarWidgetEndDate.selectedDate()
        )

    def toggle_filter_bool(self):
        # Whether or not to filter the search results
        self.filter = not self.filter

    def update_config(self):
        # Class method for updating the FID processing settings
        for key, box in zip(["exponential", "high pass", "low pass", "delay"],
                            [self.spinBoxExpFilter, self.spinBoxHighPass, self.spinBoxLowPass, self.spinBoxDelay]
                            ):
            self.config[key] = float(box.value())
        self.config["window function"] = str(self.comboBoxWindowFunction.currentText())

    def select_scan(self):
        #  Class method for selecting a scan from the table
        selected = self.tableWidgetScanChooser.currentItem()
        if selected:
            scan_number = int(selected.text())
            self.spinBoxBatchNumber.setValue(scan_number)

    def compress_data(self):
        # Uses H5Py routines to compress all of the FT data into a single HDF5
        # file. Has a progress bar that will indicate progress.
        database_filepath = QFileDialog.getSaveFileName(
            self,
            "Choose the location to save the HDF5 database.",
            os.getcwd(),
            "HDF5 files (*.h5)"
        )
        if len(database_filepath[0]) > 1:
            CompressData(
                self.dir,
                database_filepath[0],
                self.progressBarCompression
            )

    def read_latest(self):
        # Method for finding out what the most recent scan is for each Batch
        if self.root_path is not None and os.path.isdir(self.root_path) is True:
            for batch_type in ["dr", "surveys", "batch"]:
                subdir = os.path.join(self.root_path, batch_type)
                self.dir[batch_type] = glob(
                    subdir + "/*/*/*.txt"
                )
                for scan in self.dir[batch_type]:
                    ID = scan.split("/")[-1].split(".")[0]
                    self.batch_objects[batch_type][ID] = FTBatch(
                        scan,
                        batch_type,
                        self.config,
                        self.root_path,
                        peek=True
                    )

    def update_scan_table(self):
        # Method for updating the scan table, depending on the choice of batch
        # type.
        self.tableWidgetScanChooser.clear()
        self.tableWidgetScanChooser.setRowCount(0)
        choice = str(self.comboBoxScanChooser.currentText()).lower()
        if choice == "dr batch":
            choice = "dr"
        self.batch_type = choice
        self.tableWidgetScanChooser.setRowCount(len(self.dir[choice]))
        self.tableWidgetScanChooser.setColumnCount(1)

        dates = list()
        scans = list()
        # Setup the search parameters
        for calendar in [self.calendarWidgetStartDate, self.calendarWidgetEndDate]:
            dates.append(calendar.selectedDate().toPyDate())
        search_freq = float(self.doubleSpinBoxSearchFreq.value())
        # Loop over all the objects to check that they fall within the range
        if self.filter is True:
            for batch_object in (self.batch_objects[choice]):
                try:
                    hit = False
                    if self.batch_objects[batch_object]["Date"] >= dates[0] is True \
                    and self.batch_objects[batch_object]["Date"] <= dates[1] is True:
                        if search_freq != 0.:
                            # only if a search frequency is specified
                            if choice == "dr":
                                # For DR, we want to match the cavity frequency as the
                                # search criteria.
                                if np.abs(self.batch_objects[batch_object]["Cavity frequency"] - search_freq) <= 0.2:
                                    hit = True
                            elif choice == "survey":
                                # If we're looking at surveys, we want to see if the
                                # specified frequency has been covered in these surveys
                                frequencies = [self.batch_objects[batch_object]["Start frequency"],
                                               self.batch_objects[batch_object]["End frequency"]
                                               ]
                                if search_freq >= min(frequencies) and search_freq <= max(frequencies):
                                    hit = True
                        else:
                            # If we're ignoring the search frequency, just use the date
                            hit = True
                    if hit is True:
                        scans.append(batch_object["Scan ID"])
                except KeyError:
                    pass
        else:
            for scan in self.dir[choice]:
                scans.append(scan.split("/")[-1].split(".")[0])
        scans = sorted(scans, key=int)
        for index, scan in enumerate(scans):
            self.tableWidgetScanChooser.setItem(index, 0, QTableWidgetItem(str(scan)))
        self.tableWidgetScanChooser.verticalHeader().setVisible(False)

    def create_batch_object(self):
        # Create a filepath string for the ID and scan type
        id = int(self.spinBoxBatchNumber.value())
        for batch in self.dir[self.batch_type]:
            if "/" + str(id) + ".txt" in batch:
                filepath = batch
                # Once we've found our target, break out of loop
                break
        #filepath = self.root_path + "/" + self.batch_type + "/" + str(id) + ".txt"
        self.batch_object = FTBatch(filepath, self.batch_type, self.config, self.root_path, peek=False)
        self.batch_window = BatchViewerWindow(self, batch_object=self.batch_object)
        self.batch_window.show()

        #self.close_dialog()

    def close_dialog(self):
        self.close()
