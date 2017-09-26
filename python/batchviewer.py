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
        self.setupUi(self)

        self.menubar.setNativeMenuBar(False)

        self.initialize_plot()
        self.update_plot()

    def link_ui_actions(self):
        self.actionClose.triggered.connect(qApp.quit)

    def initialize_plot(self):

        # Add two main docks
        self.Overview = self.graphicsViewLayoutWidget.addPlot(
            row=1,
            col=0,
            rowspan=2
        )
        self.ROI = self.graphicsViewLayoutWidget.addPlot(
            title="Region of interest",
            row=3,
            col=0,
        )
        # Set up the region-of-interest
        self.PlotRegion = LinearRegionItem()
        self.PlotRegion.setZValue(10)
        self.Overview.addItem(self.PlotRegion, ignoreBounds = True)
        center_freq = self.batch_object.spectrum[0].mean()
        # Set the region to +/- 5% in the center
        self.PlotRegion.setRegion(
            [
                center_freq - center_freq*0.01,
                center_freq + center_freq*0.01
            ]
        )
        # Connect the ROI signal event to action
        self.PlotRegion.sigRegionChanged.connect(self.update_roi)
        self.Overview.setAutoVisible(y=True)

        # Method that will set up the PlotWidget settings
        self.graphicsViewLayoutWidget.setBackground(None)
        #self.graphicsViewLayoutWidget.setAspectLocked(False)

        for plot in [self.Overview, self.ROI]:
            for axis, label in zip(["bottom", "left"], ["Frequency (MHz)", "Intensity"]):
                plot.getAxis(axis).setLabel(label)
                plot.getAxis(axis).setPen((44,127,184))

    def update_plot(self):
        # ROI updating
        self.Overview.plot(
            self.batch_object.spectrum[0].astype(float),
            self.batch_object.spectrum[1].astype(float),
            pen=(44,127,184)
        )
        self.ROI.plot(
            self.batch_object.spectrum[0].astype(float),
            self.batch_object.spectrum[1].astype(float),
            pen=(44,127,184)
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
