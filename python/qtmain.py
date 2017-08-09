# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setObjectName("testButton")
        self.verticalLayout.addWidget(self.testButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoad = QtWidgets.QMenu(self.menuFile)
        self.menuLoad.setObjectName("menuLoad")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_spectrum = QtWidgets.QAction(MainWindow)
        self.actionLoad_spectrum.setObjectName("actionLoad_spectrum")
        self.actionSave_spectrum = QtWidgets.QAction(MainWindow)
        self.actionSave_spectrum.setObjectName("actionSave_spectrum")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDisplay_Test = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Test.setObjectName("actionDisplay_Test")
        self.actionLoad_FID = QtWidgets.QAction(MainWindow)
        self.actionLoad_FID.setObjectName("actionLoad_FID")
        self.actionSpectrum = QtWidgets.QAction(MainWindow)
        self.actionSpectrum.setObjectName("actionSpectrum")
        self.actionFID = QtWidgets.QAction(MainWindow)
        self.actionFID.setObjectName("actionFID")
        self.actionCAT = QtWidgets.QAction(MainWindow)
        self.actionCAT.setObjectName("actionCAT")
        self.menuLoad.addAction(self.actionSpectrum)
        self.menuLoad.addAction(self.actionFID)
        self.menuLoad.addAction(self.actionCAT)
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addAction(self.actionSave_spectrum)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTest.addAction(self.actionDisplay_Test)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load..."))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.actionLoad_spectrum.setText(_translate("MainWindow", "Load spectrum"))
        self.actionSave_spectrum.setText(_translate("MainWindow", "Save spectrum"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDisplay_Test.setText(_translate("MainWindow", "Display Test"))
        self.actionLoad_FID.setText(_translate("MainWindow", "Load FID"))
        self.actionSpectrum.setText(_translate("MainWindow", "Spectrum"))
        self.actionFID.setText(_translate("MainWindow", "FID"))
        self.actionCAT.setText(_translate("MainWindow", "CAT"))

from pyqtgraph import PlotWidget
