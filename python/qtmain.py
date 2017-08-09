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
        MainWindow.resize(1280, 780)
        MainWindow.setStyleSheet("#mainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(270, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tabScansettings = QtWidgets.QWidget()
        self.tabScansettings.setObjectName("tabScansettings")
        self.tabWidget.addTab(self.tabScansettings, "")
        self.tabFIDsettings = QtWidgets.QWidget()
        self.tabFIDsettings.setObjectName("tabFIDsettings")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabFIDsettings)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 258, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxWindowFunction = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBoxWindowFunction.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBoxWindowFunction.setObjectName("comboBoxWindowFunction")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxWindowFunction)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBoxExpFilter = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxExpFilter.setToolTip("")
        self.spinBoxExpFilter.setToolTipDuration(2)
        self.spinBoxExpFilter.setMaximum(1000)
        self.spinBoxExpFilter.setSingleStep(10)
        self.spinBoxExpFilter.setObjectName("spinBoxExpFilter")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxExpFilter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBoxHighPass = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxHighPass.setMaximum(1000)
        self.spinBoxHighPass.setObjectName("spinBoxHighPass")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxHighPass)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.spinBoxDelay = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxDelay.setSuffix("")
        self.spinBoxDelay.setMaximum(1000)
        self.spinBoxDelay.setObjectName("spinBoxDelay")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxDelay)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.graphicsViewFID = PlotWidget(self.verticalLayoutWidget_2)
        self.graphicsViewFID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsViewFID.setLineWidth(2)
        self.graphicsViewFID.setObjectName("graphicsViewFID")
        self.verticalLayout_2.addWidget(self.graphicsViewFID)
        self.tabWidget.addTab(self.tabFIDsettings, "")
        self.tabPeaksettings = QtWidgets.QWidget()
        self.tabPeaksettings.setObjectName("tabPeaksettings")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPeaksettings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBoxPeakSNRThres = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxPeakSNRThres.setObjectName("spinBoxPeakSNRThres")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxPeakSNRThres)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBoxPeakMinDist = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxPeakMinDist.setObjectName("spinBoxPeakMinDist")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxPeakMinDist)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.checkBoxDetectPeaks = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxDetectPeaks.setText("")
        self.checkBoxDetectPeaks.setObjectName("checkBoxDetectPeaks")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBoxDetectPeaks)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableViewPeakTable = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableViewPeakTable.setObjectName("tableViewPeakTable")
        self.verticalLayout.addWidget(self.tableViewPeakTable)
        self.tabWidget.addTab(self.tabPeaksettings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.graphicsViewMain = PlotWidget(self.centralwidget)
        self.graphicsViewMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsViewMain.setLineWidth(2)
        self.graphicsViewMain.setObjectName("graphicsViewMain")
        self.gridLayout.addWidget(self.graphicsViewMain, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 lightgray, stop:1 darkgray);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoad = QtWidgets.QMenu(self.menuFile)
        self.menuLoad.setObjectName("menuLoad")
        self.menuFitting = QtWidgets.QMenu(self.menubar)
        self.menuFitting.setObjectName("menuFitting")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFitting.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScansettings), _translate("MainWindow", "Details"))
        self.label_6.setText(_translate("MainWindow", "FID Processing"))
        self.label_7.setText(_translate("MainWindow", "Window Function"))
        self.comboBoxWindowFunction.setStatusTip(_translate("MainWindow", "Apply a window function to the FID."))
        self.comboBoxWindowFunction.setItemText(0, _translate("MainWindow", "none"))
        self.comboBoxWindowFunction.setItemText(1, _translate("MainWindow", "blackman"))
        self.comboBoxWindowFunction.setItemText(2, _translate("MainWindow", "blackmanharris"))
        self.comboBoxWindowFunction.setItemText(3, _translate("MainWindow", "boxcar"))
        self.comboBoxWindowFunction.setItemText(4, _translate("MainWindow", "hanning"))
        self.comboBoxWindowFunction.setItemText(5, _translate("MainWindow", "bartlett"))
        self.label_8.setText(_translate("MainWindow", "Exponential Filter"))
        self.spinBoxExpFilter.setStatusTip(_translate("MainWindow", "Apply an exponential filter (microseconds)"))
        self.label_9.setText(_translate("MainWindow", "High-Pass Filter"))
        self.spinBoxHighPass.setStatusTip(_translate("MainWindow", "Apply a high-pass filter (microseconds)"))
        self.label_10.setText(_translate("MainWindow", "Delay"))
        self.spinBoxDelay.setStatusTip(_translate("MainWindow", "Delay the FID processing (microseconds)"))
        self.label_11.setText(_translate("MainWindow", "FID trace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFIDsettings), _translate("MainWindow", "FID details"))
        self.label.setText(_translate("MainWindow", "Detection Settings"))
        self.label_3.setText(_translate("MainWindow", "SNR threshold"))
        self.label_4.setText(_translate("MainWindow", "Minimum distance"))
        self.label_5.setText(_translate("MainWindow", "Detect peaks"))
        self.label_2.setText(_translate("MainWindow", "Peak Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPeaksettings), _translate("MainWindow", "Peaks"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load..."))
        self.menuFitting.setTitle(_translate("MainWindow", "Fitting"))
        self.actionLoad_spectrum.setText(_translate("MainWindow", "Load spectrum"))
        self.actionSave_spectrum.setText(_translate("MainWindow", "Save spectrum"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDisplay_Test.setText(_translate("MainWindow", "Display Test"))
        self.actionLoad_FID.setText(_translate("MainWindow", "Load FID"))
        self.actionSpectrum.setText(_translate("MainWindow", "Spectrum"))
        self.actionFID.setText(_translate("MainWindow", "FID"))
        self.actionCAT.setText(_translate("MainWindow", "CAT"))

from pyqtgraph import PlotWidget
