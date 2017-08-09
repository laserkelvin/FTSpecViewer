import sys
import os
import pandas as pd
import numpy as np
import pyqtgraph
from ftclass import FTData

# Qt related modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, qApp
from QtMain import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
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

        # Exiting the program
        self.actionExit.triggered.connect(qApp.quit)

        # Processing the FIDs
        self.comboBoxWindowFunction.currentTextChanged.connect(self.process_fid)
        self.spinBoxExpFilter.valueChanged.connect(self.process_fid)
        self.spinBoxDelay.valueChanged.connect(self.process_fid)

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
        self.graphicsViewMain.setBackground("w")
        self.graphicsViewFID.setBackground("w")
        #self.graphicsViewMain.addLegend()

        for axis, label in zip(["bottom", "left"], ["Frequency (MHz)", "Intensity"]):
            self.graphicsViewMain.getAxis(axis).setLabel(label)

        for axis, label in zip(["bottom", "left"], ["Time (us)", "FID"]):
            self.graphicsViewFID.getAxis(axis).setLabel(label)

    def update_plot(self):
        # Method to plot the current spectrum
        self.graphicsViewMain.clear()
        self.graphicsViewMain.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Intensity"].astype(float),
                pen=(99,99,99),
                name="Spectrum"
            )
        if self.fid is True:
            self.graphicsViewFID.clear()
            self.graphicsViewFID.plot(
                self.data.fid_df["Time"].astype(float),
                self.data.fid_df["FID"].astype(float),
                pen=(99,99,99),
                name="FID"
            )

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

        except FileNotFoundError:
            self.statusBar.showMessage("File not found!")
