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
from pyqtgraph import dockarea, PlotWidget, LinearRegionItem, GraphicsLayoutWidget
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

        self.menubar.setNativeMenuBar(False)

        self.initialize_plot()
        self.update_plot()

    def link_ui_actions(self):
        self.actionClose.triggered.connect(qApp.quit)

    def initialize_plot(self):
        # Add two main docks
        self.MainDock = dockarea.Dock(name="Main plot", size=(800,400))
        self.FFTDock = dockarea.Dock(name="FFT", size=(150,150))
        self.graphicsViewDockArea.addDock(self.MainDock)
        self.graphicsViewDockArea.addDock(self.FFTDock, "top", self.MainDock)

        self.MainPlotWidget = GraphicsLayoutWidget()
        self.ROI = self.MainPlotWidget.addPlot(row=1, col=1, colspan=1, title="ROI")
        self.Overview = self.MainPlotWidget.addPlot(row=2, col=1, colspan=2, title="Overview")
        self.MainPlotRegion = LinearRegionItem()
        self.Overview.addItem(self.MainPlotRegion, ignoreBounds = True)

        self.MainDock.addWidget(self.MainPlotWidget)
        self.MainPlotRegion.sigRegionChanged.connect(self.update_roi)

        qGraphicsGridLayout = self.MainPlotWidget.ci.layout
        qGraphicsGridLayout.setColumnStretchFactor(0, 2)
        qGraphicsGridLayout.setColumnStretchFactor(1, 1)

        self.FFTPlot = PlotWidget()
        self.FFTPlot.plot(np.random.normal(size=50))
        self.FFTDock.addWidget(self.FFTPlot)

    def update_plot(self):
        self.Overview.plot(
            self.batch_object.spectrum[0].astype(float),
            self.batch_object.spectrum[1].astype(float),
        )
        self.ROI.plot(
            self.batch_object.spectrum[0].astype(float),
            self.batch_object.spectrum[1].astype(float),
        )

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
