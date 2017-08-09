import sys
import os
import pandas as pd
import numpy as np
import pyqtgraph
from ftclass import FTData

# Qt related modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from QtMain import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)
        self.link_actions()

    def link_actions(self):
        self.testButton.clicked.connect(self.plot_random)
        self.actionSpectrum.triggered.connect(self.load_spectrum)
        self.actionFID.triggered.connect(self.load_FID)

    def plot_random(self):
        self.graphicsView.clear()
        x = np.linspace(-10., 10., 100)
        y = np.random.rand(100)
        self.graphicsView.plot(x, y)

    def update_plot(self):
        xax = self.graphicsView.getAxis('bottom')
        xax.setLabel("Frequency (MHz)")
        self.graphicsView.clear()
        self.graphicsView.plot(
                self.data.spectrum["Frequency"].astype(float),
                self.data.spectrum["Intensity"].astype(float),
            )

    def load_spectrum(self):
        filepath = QFileDialog.getOpenFileName(self, "Open a spectrum file")

        try:
            self.data = FTData(filepath[0], fid=False)
            self.fid = False
            self.update_plot()
        except FileNotFoundError:
            pass

    def load_FID(self):
        filepath = QFileDialog.getOpenFileName(self, "Open a FID file")

        try:
            self.data = FTData(filepath[0], fid=True)
            self.fid = True
            self.data.fid2fft()
            self.update_plot()
        except FileNotFoundError:
            pass
