"""
A dedicated batch viewer class. This class is called by the main window when
a specific batch/survey is selected via the ScanChooserWindow.
"""

# PIP and system modules
import sys
import os
import pandas as pd
import numpy as np
import yaml
from uncertainties import ufloat, unumpy
from pyqtgraph import PlotWidget, LinearRegionItem, GraphicsLayoutWidget
from glob import glob
from matplotlib import pyplot as plt

# Non-PIP modules

from ftclass import FTData
import fittingroutines as fr

# Qt modules

from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, qApp,
                             QTableWidgetItem)
from qtbatch import Ui_BatchViewer
from fonts_rc import *


class BatchViewerWindow(QMainWindow, Ui_BatchViewer):
    def __init__(self, parent=None, batch_object=None):
        super(BatchViewerWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.peaks = None
        self.peaks_df = None

        self.batch_object = batch_object
        self.confine_fit_region = False

        self.plotitems = {"ROI": dict(), "Overview": dict()}
        self.setupUi(self)
        self.link_ui_actions()

        self.menubar.setNativeMenuBar(False)

        self.initialize_plot()
        self.update_plot()

    def link_ui_actions(self):
        # Currently not working!
        self.actionClose.triggered.connect(self.close)
        # Reprocess FIDs button
        self.pushButtonReprocess.clicked.connect(self.reprocess_fids)
        # Fit DR buttons
        self.pushButtonFitDR.clicked.connect(self.fit_dr)

    def initialize_plot(self):

        # Add two main docks
        self.Overview = self.graphicsViewLayoutWidget.addPlot(
            row=1,
            col=1,
            rowspan=2,
            colspan=3
        )
        self.FFT = self.graphicsViewLayoutWidget.addPlot(
            title="FFT",
            row=3,
            col=1
        )
        self.ROI = self.graphicsViewLayoutWidget.addPlot(
            title="Region of interest",
            row=3,
            col=2,
            colspan=2
        )
        # Set up the region-of-interest
        self.PlotRegion = LinearRegionItem()
        self.PlotRegion.setZValue(10)
        self.Overview.addItem(self.PlotRegion, ignoreBounds = True)
        center_freq = np.average(
            [
                self.batch_object.spectrum["Frequency"].min(),
                self.batch_object.spectrum["Frequency"].max()
            ]
        )
        freq_range = np.abs(
            self.batch_object.spectrum["Frequency"].min() - \
            self.batch_object.spectrum["Frequency"].max()
        )
        # Set the region to +/- 10% in the center
        self.PlotRegion.setRegion(
            [
                center_freq - freq_range * 0.1,
                center_freq + freq_range * 0.1
            ]
        )
        # Connect the ROI signal event to action
        self.PlotRegion.sigRegionChanged.connect(self.update_roi)
        self.Overview.setAutoVisible(y=True)
        self.Overview.addLegend()

        # Method that will set up the PlotWidget settings
        self.graphicsViewLayoutWidget.setBackground(None)
        #self.graphicsViewLayoutWidget.setAspectLocked(False)

        for plot in [self.Overview, self.ROI]:
            for axis, label in zip(["bottom", "left"], ["Frequency (MHz)", "Intensity"]):
                plot.getAxis(axis).setLabel(label)
                plot.getAxis(axis).setPen((44,127,184))

    def update_plot(self):
        # ROI updating
        plot_labels = [key for key in self.batch_object.spectrum.keys() if key != "Frequency"]
        colors = plt.cm.RdYlBu(np.linspace(0, 1, len(plot_labels))) * 255
        for color, plot in zip(colors, plot_labels):
            if plot not in self.plotitems["Overview"].keys():
                self.plotitems["Overview"][plot] = self.Overview.plot(
                    self.batch_object.spectrum["Frequency"].astype(float),
                    self.batch_object.spectrum[plot].astype(float),
                    pen=color[:-1].astype(int),
                    name=plot
                )
                self.plotitems["ROI"][plot] = self.ROI.plot(
                    self.batch_object.spectrum["Frequency"].astype(float),
                    self.batch_object.spectrum[plot].astype(float),
                    pen=color[:-1].astype(int),
                    name=plot
                )
            else:
                self.plotitems["Overview"][plot].setData(
                    self.batch_object.spectrum["Frequency"].astype(float),
                    self.batch_object.spectrum[plot].astype(float),
                    pen=color[:-1].astype(int),
                    name=plot
                )
                self.plotitems["ROI"][plot].setData(
                    self.batch_object.spectrum["Frequency"].astype(float),
                    self.batch_object.spectrum[plot].astype(float),
                    pen=color[:-1].astype(int),
                    name=plot
                )


    def update_roi(self):
        # Update the region-of-interest plot when the region is changed in the
        # overview plot
        self.PlotRegion.setZValue(10)
        minX, maxX = self.PlotRegion.getRegion()
        self.ROI.setXRange(minX, maxX, padding=0)

    def update_region(self, window, viewRange):
        # Updates the region indicator in the overview plot when the focus is
        # changed in the ROI plot
        rgn = viewRange[0]
        self.PlotRegion.setRegion(rgn)

    def update_config(self):
        # Class method for updating the FID processing settings
        for key, box in zip(["exponential", "high pass", "low pass", "delay"],
                            [self.spinBoxExpFilter, self.spinBoxHighPass, self.spinBoxLowPass, self.spinBoxDelay]
                            ):
            self.config[key] = float(box.value())
        self.config["window function"] = str(self.comboBoxWindowFunction.currentText())

    def reprocess_fids(self):
        self.update_config()
        self.batch_object.fidsettings.update(self.config)
        self.batch_object.process_all_fids()

    def toggle_confine_bool(self):
        self.confine_fit_region = not self.confine_fit_region

    def fit_dr(self):
        if self.confine_fit_region is True:
            freq_range = self.PlotRegion.getRegion()
        else:
            freq_range = None
        # Check the SavGol parameters to make sure they're valid
        savgol_window = int(self.spinBoxSavgolWindow.value())
        savgol_polynomial = int(self.spinBoxSavgolPolynomial.value())
        if savgol_window >= 0 and savgol_polynomial <= savgol_window:
            if savgol_window % 2 > 0:
                if savgol_polynomial % 2 > 0:
                    savgol = [savgol_window, savgol_polynomial]
                else:
                    savgol = [0, 0]
            else:
                savgol = [0, 0]
        else:
            savgol = [0, 0]
        self.batch_object.fit_dr(freq_range, savgol)
        self.labelDRFreq.setText(
            "{:.3uS}".format(self.batch_object.fit_results["Center"])
        )
        self.labelFWHM.setText(
            str(self.batch_object.fit_results["Width"] * 2.355)
        )
        self.update_plot()

    def save_spectrum(self):
        if self.data:
            filepath = QFileDialog.getSaveFileName(self, "Save the spectrum")
            if filepath:
                self.batch_object.spectrum.to_csv(filepath[0], index=False)
