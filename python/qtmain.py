# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 849)
        MainWindow.setStyleSheet("QMainWindow {\n"
" background-color: #ffffff;\n"
" font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QMenuBar {\n"
" background-color: #ffffff;\n"
" color: #ffffff;\n"
" font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QMenuBar::item {\n"
" color: #2c7fb8;\n"
" border-radius: 4px\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" color: #2c7fb8\n"
"}\n"
"\n"
"QPushButton {\n"
" background-color: #FFFFFF;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border: 1.5px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"min-width: 10ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: 500;\n"
"font-size: 15px;\n"
"color: #2c7fb8;\n"
"}\n"
"\n"
"QWidget {\n"
" background-color: #ffffff\n"
"}\n"
"\n"
"QTabWidget {\n"
"background-color: #ffffff\n"
"}\n"
"\n"
"QLabel {\n"
"color: #2c7fb8;\n"
"font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    color: #2c7fb8;\n"
"    font-size: 15px;\n"
"border: 1.5px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"min-width: 10ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    color: #2c7fb8;\n"
"    font-size: 15px;\n"
"border: 1.5px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"min-width: 10ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: #FFFFFF;\n"
"color: #2c7fb8;\n"
"font-size: 15px;\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background: #FFFFFF;\n"
"color: #2c7fb8;\n"
"border: 2px solid #FFFFFF;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #edf8b1;\n"
"color: #2c7fb8;\n"
"font-family: \'Roboto\';\n"
"font-weight: 600\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #edf8b1;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"QTableWidget {\n"
" background-color: #FFFFFF;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border: 1.5px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"min-width: 10ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: 500;\n"
"font-size: 15px;\n"
"color: #2c7fb8;\n"
"}\n"
"\n"
"QGraphicsView {\n"
"font-family: \'Robot\', sans-serif;\n"
"font-size: 15px\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsViewMain = PlotWidget(self.centralwidget)
        self.graphicsViewMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsViewMain.setLineWidth(2)
        self.graphicsViewMain.setObjectName("graphicsViewMain")
        self.verticalLayout_5.addWidget(self.graphicsViewMain)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.graphicsViewFID = PlotWidget(self.centralwidget)
        self.graphicsViewFID.setMaximumSize(QtCore.QSize(16777215, 230))
        self.graphicsViewFID.setObjectName("graphicsViewFID")
        self.verticalLayout_5.addWidget(self.graphicsViewFID)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(285, 16777215))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabScansettings = QtWidgets.QWidget()
        self.tabScansettings.setObjectName("tabScansettings")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tabScansettings)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 251, 671))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.labelScanNum = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelScanNum.setMinimumSize(QtCore.QSize(100, 0))
        self.labelScanNum.setMaximumSize(QtCore.QSize(100, 30))
        self.labelScanNum.setFrameShape(QtWidgets.QFrame.Box)
        self.labelScanNum.setLineWidth(1)
        self.labelScanNum.setText("")
        self.labelScanNum.setObjectName("labelScanNum")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelScanNum)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.labelShotCount = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelShotCount.setMinimumSize(QtCore.QSize(100, 0))
        self.labelShotCount.setMaximumSize(QtCore.QSize(100, 30))
        self.labelShotCount.setFrameShape(QtWidgets.QFrame.Box)
        self.labelShotCount.setText("")
        self.labelShotCount.setObjectName("labelShotCount")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelShotCount)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.labelTuning = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelTuning.setMinimumSize(QtCore.QSize(100, 0))
        self.labelTuning.setMaximumSize(QtCore.QSize(100, 30))
        self.labelTuning.setFrameShape(QtWidgets.QFrame.Box)
        self.labelTuning.setText("")
        self.labelTuning.setObjectName("labelTuning")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTuning)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.labelAttenuation = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelAttenuation.setMinimumSize(QtCore.QSize(100, 0))
        self.labelAttenuation.setMaximumSize(QtCore.QSize(100, 30))
        self.labelAttenuation.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAttenuation.setText("")
        self.labelAttenuation.setObjectName("labelAttenuation")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelAttenuation)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.tabWidget.addTab(self.tabScansettings, "")
        self.tabFIDsettings = QtWidgets.QWidget()
        self.tabFIDsettings.setObjectName("tabFIDsettings")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabFIDsettings)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 282, 750))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxWindowFunction = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBoxWindowFunction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxWindowFunction.setObjectName("comboBoxWindowFunction")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxWindowFunction)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBoxExpFilter = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxExpFilter.setToolTip("")
        self.spinBoxExpFilter.setToolTipDuration(2)
        self.spinBoxExpFilter.setMaximum(1000)
        self.spinBoxExpFilter.setSingleStep(10)
        self.spinBoxExpFilter.setObjectName("spinBoxExpFilter")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxExpFilter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBoxHighPass = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxHighPass.setMaximum(1000)
        self.spinBoxHighPass.setSingleStep(5)
        self.spinBoxHighPass.setProperty("value", 0)
        self.spinBoxHighPass.setObjectName("spinBoxHighPass")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxHighPass)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.spinBoxLowPass = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxLowPass.setMaximum(1000)
        self.spinBoxLowPass.setSingleStep(5)
        self.spinBoxLowPass.setProperty("value", 0)
        self.spinBoxLowPass.setObjectName("spinBoxLowPass")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxLowPass)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.spinBoxDelay = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxDelay.setSuffix("")
        self.spinBoxDelay.setMaximum(1000)
        self.spinBoxDelay.setObjectName("spinBoxDelay")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBoxDelay)
        self.spinBoxScanID = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxScanID.setMaximum(10000000)
        self.spinBoxScanID.setObjectName("spinBoxScanID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBoxScanID)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.pushButtonPickDoppler = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonPickDoppler.setObjectName("pushButtonPickDoppler")
        self.verticalLayout_2.addWidget(self.pushButtonPickDoppler)
        self.pushButtonAutofit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonAutofit.setObjectName("pushButtonAutofit")
        self.verticalLayout_2.addWidget(self.pushButtonAutofit)
        self.tableWidgetDopplerPeaks = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidgetDopplerPeaks.setObjectName("tableWidgetDopplerPeaks")
        self.tableWidgetDopplerPeaks.setColumnCount(0)
        self.tableWidgetDopplerPeaks.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidgetDopplerPeaks)
        self.tabWidget.addTab(self.tabFIDsettings, "")
        self.tabPeaksettings = QtWidgets.QWidget()
        self.tabPeaksettings.setObjectName("tabPeaksettings")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPeaksettings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.checkBoxDetectPeaks = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxDetectPeaks.setText("")
        self.checkBoxDetectPeaks.setObjectName("checkBoxDetectPeaks")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBoxDetectPeaks)
        self.doubleSpinBoxPeakSNRThres = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxPeakSNRThres.setMaximum(10.0)
        self.doubleSpinBoxPeakSNRThres.setSingleStep(0.01)
        self.doubleSpinBoxPeakSNRThres.setProperty("value", 0.3)
        self.doubleSpinBoxPeakSNRThres.setObjectName("doubleSpinBoxPeakSNRThres")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPeakSNRThres)
        self.doubleSpinBoxPeakMinDist = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxPeakMinDist.setProperty("value", 1.0)
        self.doubleSpinBoxPeakMinDist.setObjectName("doubleSpinBoxPeakMinDist")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPeakMinDist)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableWidgetPeakTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidgetPeakTable.setObjectName("tableWidgetPeakTable")
        self.tableWidgetPeakTable.setColumnCount(0)
        self.tableWidgetPeakTable.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidgetPeakTable)
        self.tabWidget.addTab(self.tabPeaksettings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
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
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuFitting = QtWidgets.QMenu(self.menubar)
        self.menuFitting.setObjectName("menuFitting")
        self.menuOverlays = QtWidgets.QMenu(self.menubar)
        self.menuOverlays.setObjectName("menuOverlays")
        self.menuLoad_overlay = QtWidgets.QMenu(self.menuOverlays)
        self.menuLoad_overlay.setObjectName("menuLoad_overlay")
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
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionCAT_file = QtWidgets.QAction(MainWindow)
        self.actionCAT_file.setObjectName("actionCAT_file")
        self.actionPeaks = QtWidgets.QAction(MainWindow)
        self.actionPeaks.setObjectName("actionPeaks")
        self.actionSave_FID = QtWidgets.QAction(MainWindow)
        self.actionSave_FID.setObjectName("actionSave_FID")
        self.actionSave_peaks = QtWidgets.QAction(MainWindow)
        self.actionSave_peaks.setObjectName("actionSave_peaks")
        self.actionFit_Gaussian = QtWidgets.QAction(MainWindow)
        self.actionFit_Gaussian.setCheckable(False)
        self.actionFit_Gaussian.setObjectName("actionFit_Gaussian")
        self.actionPick_Gaussians = QtWidgets.QAction(MainWindow)
        self.actionPick_Gaussians.setObjectName("actionPick_Gaussians")
        self.actionBatch = QtWidgets.QAction(MainWindow)
        self.actionBatch.setObjectName("actionBatch")
        self.actionDR_scan = QtWidgets.QAction(MainWindow)
        self.actionDR_scan.setObjectName("actionDR_scan")
        self.actionManual_FFT_peaks = QtWidgets.QAction(MainWindow)
        self.actionManual_FFT_peaks.setObjectName("actionManual_FFT_peaks")
        self.actionFFT_fits = QtWidgets.QAction(MainWindow)
        self.actionFFT_fits.setObjectName("actionFFT_fits")
        self.actionOverlay_settings = QtWidgets.QAction(MainWindow)
        self.actionOverlay_settings.setObjectName("actionOverlay_settings")
        self.actionLegacy_mmw = QtWidgets.QAction(MainWindow)
        self.actionLegacy_mmw.setObjectName("actionLegacy_mmw")
        self.actionFTB = QtWidgets.QAction(MainWindow)
        self.actionFTB.setObjectName("actionFTB")
        self.actionSave_peaks_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_peaks_2.setObjectName("actionSave_peaks_2")
        self.actionStick_spectrum = QtWidgets.QAction(MainWindow)
        self.actionStick_spectrum.setObjectName("actionStick_spectrum")
        self.actionCompress_data = QtWidgets.QAction(MainWindow)
        self.actionCompress_data.setObjectName("actionCompress_data")
        self.actionQtFTMScan = QtWidgets.QAction(MainWindow)
        self.actionQtFTMScan.setObjectName("actionQtFTMScan")
        self.actionCreate_batch = QtWidgets.QAction(MainWindow)
        self.actionCreate_batch.setObjectName("actionCreate_batch")
        self.menuLoad.addAction(self.actionSpectrum)
        self.menuLoad.addAction(self.actionFID)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.actionBatch)
        self.menuLoad.addAction(self.actionLegacy_mmw)
        self.menuExport.addAction(self.actionFTB)
        self.menuExport.addAction(self.actionSave_peaks_2)
        self.menuExport.addAction(self.actionStick_spectrum)
        self.menuFile.addAction(self.actionCreate_batch)
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_FID)
        self.menuFile.addAction(self.actionSave_spectrum)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuFitting.addAction(self.actionFit_Gaussian)
        self.menuFitting.addAction(self.actionManual_FFT_peaks)
        self.menuFitting.addAction(self.actionPick_Gaussians)
        self.menuFitting.addSeparator()
        self.menuLoad_overlay.addAction(self.actionCAT_file)
        self.menuLoad_overlay.addAction(self.actionPeaks)
        self.menuOverlays.addAction(self.menuLoad_overlay.menuAction())
        self.menuOverlays.addAction(self.actionOverlay_settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFitting.menuAction())
        self.menubar.addAction(self.menuOverlays.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTSpecViewer"))
        self.graphicsViewMain.setStatusTip(_translate("MainWindow", "Main spectrum window"))
        self.label_11.setText(_translate("MainWindow", "FID trace"))
        self.graphicsViewFID.setStatusTip(_translate("MainWindow", "Overview window"))
        self.label_16.setText(_translate("MainWindow", "Scan Details"))
        self.label_12.setText(_translate("MainWindow", "Scan number"))
        self.label_13.setText(_translate("MainWindow", "Shot count"))
        self.label_14.setText(_translate("MainWindow", "Tuning voltage"))
        self.label_15.setText(_translate("MainWindow", "Attenuation"))
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
        self.spinBoxHighPass.setStatusTip(_translate("MainWindow", "Apply a high-pass filter (kHz)"))
        self.label_18.setText(_translate("MainWindow", "Low-Pass Filter"))
        self.spinBoxLowPass.setStatusTip(_translate("MainWindow", "Apply a low-pass filter (kHz)"))
        self.label_10.setText(_translate("MainWindow", "Delay"))
        self.spinBoxDelay.setStatusTip(_translate("MainWindow", "Delay the FID processing (microseconds)"))
        self.label_19.setText(_translate("MainWindow", "Scan ID"))
        self.pushButtonPickDoppler.setText(_translate("MainWindow", "Manual Doppler fit"))
        self.pushButtonAutofit.setText(_translate("MainWindow", "Autofit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFIDsettings), _translate("MainWindow", "FID details"))
        self.label.setText(_translate("MainWindow", "Detection Settings"))
        self.label_3.setText(_translate("MainWindow", "Threshold"))
        self.label_4.setText(_translate("MainWindow", "Minimum distance"))
        self.label_5.setText(_translate("MainWindow", "Detect peaks"))
        self.checkBoxDetectPeaks.setStatusTip(_translate("MainWindow", "Check to automatically detect peaks"))
        self.doubleSpinBoxPeakSNRThres.setStatusTip(_translate("MainWindow", "Minimum SNR value for peak detection"))
        self.doubleSpinBoxPeakMinDist.setStatusTip(_translate("MainWindow", "Minimum distance between detected peaks"))
        self.label_2.setText(_translate("MainWindow", "Peak Table"))
        self.tableWidgetPeakTable.setStatusTip(_translate("MainWindow", "Table of detected peaks in the spectrum"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPeaksettings), _translate("MainWindow", "Peaks"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load..."))
        self.menuExport.setTitle(_translate("MainWindow", "Export peaks..."))
        self.menuFitting.setTitle(_translate("MainWindow", "Fitting"))
        self.menuOverlays.setTitle(_translate("MainWindow", "Overlays"))
        self.menuLoad_overlay.setTitle(_translate("MainWindow", "Load overlay..."))
        self.actionLoad_spectrum.setText(_translate("MainWindow", "Load spectrum"))
        self.actionSave_spectrum.setText(_translate("MainWindow", "Save spectrum"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDisplay_Test.setText(_translate("MainWindow", "Display Test"))
        self.actionLoad_FID.setText(_translate("MainWindow", "Load FID"))
        self.actionSpectrum.setText(_translate("MainWindow", "Spectrum"))
        self.actionFID.setText(_translate("MainWindow", "FID"))
        self.actionFID.setToolTip(_translate("MainWindow", "FID"))
        self.actionFID.setStatusTip(_translate("MainWindow", "Load FIDs. If several are loaded at the same time, it will co-average them."))
        self.actionCAT.setText(_translate("MainWindow", "CAT"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionCAT_file.setText(_translate("MainWindow", "CAT file"))
        self.actionCAT_file.setStatusTip(_translate("MainWindow", "Load an SPCAT catalog file."))
        self.actionPeaks.setText(_translate("MainWindow", "Peaks"))
        self.actionPeaks.setStatusTip(_translate("MainWindow", "Load a plain text file containing frequencies and intensities"))
        self.actionSave_FID.setText(_translate("MainWindow", "Save FID"))
        self.actionSave_peaks.setText(_translate("MainWindow", "Save peaks"))
        self.actionFit_Gaussian.setText(_translate("MainWindow", "Autofit FFT peaks"))
        self.actionPick_Gaussians.setText(_translate("MainWindow", "Pick Gaussians"))
        self.actionBatch.setText(_translate("MainWindow", "Batch"))
        self.actionDR_scan.setText(_translate("MainWindow", "DR scan"))
        self.actionManual_FFT_peaks.setText(_translate("MainWindow", "Manual FFT peaks"))
        self.actionFFT_fits.setText(_translate("MainWindow", "FFT fitting"))
        self.actionOverlay_settings.setText(_translate("MainWindow", "Overlay settings"))
        self.actionLegacy_mmw.setText(_translate("MainWindow", "Legacy mmw"))
        self.actionFTB.setText(_translate("MainWindow", "FTB"))
        self.actionSave_peaks_2.setText(_translate("MainWindow", "ASCII"))
        self.actionStick_spectrum.setText(_translate("MainWindow", "Stick spectrum"))
        self.actionCompress_data.setText(_translate("MainWindow", "Compress data"))
        self.actionQtFTMScan.setText(_translate("MainWindow", "QtFTM Scan"))
        self.actionCreate_batch.setText(_translate("MainWindow", "Create batch"))

from pyqtgraph import PlotWidget
import fonts_rc
