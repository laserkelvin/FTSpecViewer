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
from pyqtgraph import dockarea, PlotWidget, LinearRegionItem
from glob import glob

from ftclass import FTData
import fittingroutines as fr

from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, qApp,
                             QTableWidgetItem)
from qtbatch import Ui_BatchViewer

class BatchViewerWindow(QMainWindow, Ui_BatchViewer):
    def __init__(self, parent=None, batch_object=None):
        super(BatchViewerWindow, self).__init__(parent)

        # initialize some class data
        self.detect_peaks_bool = False
        self.peaks = None
        self.peaks_df = None

        self.batch_object = batch_object
        self.setupUi(self)

    def link_ui_actions(self):
        self.actionClose.triggered.connect(self.close_window)

    def initialize_plot(self):
        # Add two main docks
        self.MainDock = dockarea.Dock(size=(800,400))
        self.FFTDock = dockarea.Dock(size=(150,150))
        self.graphicsViewDockArea.addDock(self.MainDock)
        self.graphicsViewDockArea.addDock(self.FFTDock, "top", self.MainDock)

        self.MainPlot = PlotWidget()
        self.ROI = self.MainPlot.addPlot(row=1, col=0)
        self.Overview = self.MainPlot.addPlot(row=2, col=0)
        self.MainPlotRegion = LinearRegionItem()
        self.Overview.addItem(self.MainPlotRegion, ignoreBounds = True)
        self.MainDock.addWidget(self.MainPlot)
        self.MainPlotRegion.sigRegionChanged.connect(self.update_roi)

        self.FFTPlot = PlotWidget()
        self.FFTPlot.plot(np.random.normal(size=50))
        self.FFTDock.addWidget(self.FFTPlot)

    def update_roi(self):
        # Update the region-of-interest plot when the region is changed in the
        # overview plot
        minX, maxX = self.MainPlotRegion.getRegion()
        self.ROI.setXRange(minX, maxX, padding=0)

    def update_region(self, window, viewRange):
        # Updates the region indicator in the overview plot when the focus is
        # changed in the ROI plot
        rgn = viewRange[0]
        self.MainPlotRegion.setRegion(rgn)

    def close_window(self):
        self.close()
