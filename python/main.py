import sys
import os
import pandas as pd
import numpy as np
import pyqtgraph

from ftclass import FTData
import fittingroutines as fr

# Qt related modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, qApp, QTableWidgetItem
from qtmain import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.data = None
        self.peaks = None
        self.peaks_df = None

        self.setupUi(self)
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

        # Exiting the program
        self.actionExit.triggered.connect(qApp.quit)

        # Processing the FIDs
        self.comboBoxWindowFunction.currentTextChanged.connect(self.process_fid)
        self.spinBoxExpFilter.valueChanged.connect(self.process_fid)
        self.spinBoxDelay.valueChanged.connect(self.process_fid)

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
        self.tableWidgetPeakTable.setRowCount(len(self.peaks))
        self.tableWidgetPeakTable.setColumnCount(2)
        for index, header in enumerate(["Frequency", "Intensity"]):
            self.tableWidgetPeakTable.setHorizontalHeaderItem(index, QTableWidgetItem(header))
        for peak_num, peak in enumerate(self.peaks):
            self.tableWidgetPeakTable.insertRow(peak_num)
            for index, value in enumerate(peak):
                self.tableWidgetPeakTable.setItem(peak_num, index, QTableWidgetItem("{:.4}".format(value)))

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
        self.graphicsViewMain.setAspectLocked(False)
        self.graphicsViewFID.setAspectLocked(False)
        self.graphicsViewMain.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Intensity"].astype(float),
                pen=(7,136,155),
                name="Spectrum"
            )
        if "Fit" in list(self.data.spectrum.keys()):
            self.graphicsViewMain.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Fit"].astype(float),
                pen=(227,114,34),
                name="Fit"
            )
        if self.peaks_df is not None and self.detect_peaks_bool is True:
            peak_plot = pyqtgraph.ScatterPlotItem(
                x=self.peaks_df["Frequency"].astype(float),
                y=self.peaks_df["Intensity"].astype(float),
                pen=(238,170,123),
                name="Peaks"
            )
            self.graphicsViewMain.addItem(peak_plot)
            self.statusBar.showMessage("Plotting the peaks...")
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
