# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatchViewer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchViewer(object):
    def setupUi(self, BatchViewer):
        BatchViewer.setObjectName("BatchViewer")
        BatchViewer.resize(1083, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchViewer.sizePolicy().hasHeightForWidth())
        BatchViewer.setSizePolicy(sizePolicy)
        BatchViewer.setMinimumSize(QtCore.QSize(0, 0))
        BatchViewer.setMaximumSize(QtCore.QSize(16777215, 700))
        BatchViewer.setStyleSheet("QMainWindow {\n"
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
        self.centralwidget = QtWidgets.QWidget(BatchViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsViewLayoutWidget = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsViewLayoutWidget.setGeometry(QtCore.QRect(270, 10, 800, 600))
        self.graphicsViewLayoutWidget.setObjectName("graphicsViewLayoutWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 241, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 231, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxWindowFunction = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxWindowFunction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxWindowFunction.setObjectName("comboBoxWindowFunction")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxWindowFunction)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBoxExpFilter = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxExpFilter.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxExpFilter.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBoxExpFilter.setToolTip("")
        self.spinBoxExpFilter.setToolTipDuration(2)
        self.spinBoxExpFilter.setMaximum(1000)
        self.spinBoxExpFilter.setSingleStep(10)
        self.spinBoxExpFilter.setObjectName("spinBoxExpFilter")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxExpFilter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBoxHighPass = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxHighPass.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxHighPass.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBoxHighPass.setMaximum(190)
        self.spinBoxHighPass.setObjectName("spinBoxHighPass")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxHighPass)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.spinBoxDelay = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxDelay.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxDelay.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBoxDelay.setSuffix("")
        self.spinBoxDelay.setMaximum(1000)
        self.spinBoxDelay.setObjectName("spinBoxDelay")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxDelay)
        self.spinBoxScanNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxScanNumber.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxScanNumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBoxScanNumber.setMinimum(0)
        self.spinBoxScanNumber.setMaximum(9999999)
        self.spinBoxScanNumber.setProperty("value", 0)
        self.spinBoxScanNumber.setObjectName("spinBoxScanNumber")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBoxScanNumber)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.spinBoxLowPass = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxLowPass.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxLowPass.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBoxLowPass.setMaximum(190)
        self.spinBoxLowPass.setObjectName("spinBoxLowPass")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxLowPass)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.pushButtonReprocess = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/reload-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReprocess.setIcon(icon)
        self.pushButtonReprocess.setObjectName("pushButtonReprocess")
        self.verticalLayout.addWidget(self.pushButtonReprocess)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAddRegion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButtonAddRegion.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/plus-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddRegion.setIcon(icon1)
        self.pushButtonAddRegion.setObjectName("pushButtonAddRegion")
        self.horizontalLayout.addWidget(self.pushButtonAddRegion)
        self.pushButtonRemoveRegion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/minus-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRemoveRegion.setIcon(icon2)
        self.pushButtonRemoveRegion.setObjectName("pushButtonRemoveRegion")
        self.horizontalLayout.addWidget(self.pushButtonRemoveRegion)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.checkBoxConfine = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxConfine.setText("")
        self.checkBoxConfine.setObjectName("checkBoxConfine")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBoxConfine)
        self.spinBoxSavgolWindow = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxSavgolWindow.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxSavgolWindow.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBoxSavgolWindow.setMaximum(21)
        self.spinBoxSavgolWindow.setSingleStep(1)
        self.spinBoxSavgolWindow.setObjectName("spinBoxSavgolWindow")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxSavgolWindow)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.spinBoxSavgolPolynomial = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxSavgolPolynomial.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxSavgolPolynomial.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBoxSavgolPolynomial.setMaximum(19)
        self.spinBoxSavgolPolynomial.setSingleStep(1)
        self.spinBoxSavgolPolynomial.setObjectName("spinBoxSavgolPolynomial")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxSavgolPolynomial)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.pushButtonFitDR = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/magnifying-glass-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFitDR.setIcon(icon3)
        self.pushButtonFitDR.setObjectName("pushButtonFitDR")
        self.verticalLayout.addWidget(self.pushButtonFitDR)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelDRFreq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDRFreq.setMinimumSize(QtCore.QSize(100, 0))
        self.labelDRFreq.setText("")
        self.labelDRFreq.setObjectName("labelDRFreq")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelDRFreq)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.labelFWHM = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelFWHM.setMinimumSize(QtCore.QSize(100, 0))
        self.labelFWHM.setText("")
        self.labelFWHM.setObjectName("labelFWHM")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelFWHM)
        self.verticalLayout.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 231, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.checkBoxDetectPeaks_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxDetectPeaks_3.setText("")
        self.checkBoxDetectPeaks_3.setObjectName("checkBoxDetectPeaks_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBoxDetectPeaks_3)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.doubleSpinBoxPeakSNRThres_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBoxPeakSNRThres_3.setMaximum(10.0)
        self.doubleSpinBoxPeakSNRThres_3.setSingleStep(0.01)
        self.doubleSpinBoxPeakSNRThres_3.setProperty("value", 0.3)
        self.doubleSpinBoxPeakSNRThres_3.setObjectName("doubleSpinBoxPeakSNRThres_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPeakSNRThres_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.doubleSpinBoxPeakMinDist_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBoxPeakMinDist_3.setProperty("value", 1.0)
        self.doubleSpinBoxPeakMinDist_3.setObjectName("doubleSpinBoxPeakMinDist_3")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPeakMinDist_3)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidgetPeakTable = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidgetPeakTable.setObjectName("tableWidgetPeakTable")
        self.tableWidgetPeakTable.setColumnCount(0)
        self.tableWidgetPeakTable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidgetPeakTable)
        self.tabWidget.addTab(self.tab_2, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 10, 20, 601))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        BatchViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BatchViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOverlays = QtWidgets.QMenu(self.menubar)
        self.menuOverlays.setObjectName("menuOverlays")
        self.menuLoad_overlay = QtWidgets.QMenu(self.menuOverlays)
        self.menuLoad_overlay.setObjectName("menuLoad_overlay")
        self.menuScan_details = QtWidgets.QMenu(self.menubar)
        self.menuScan_details.setObjectName("menuScan_details")
        BatchViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BatchViewer)
        self.statusbar.setObjectName("statusbar")
        BatchViewer.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(BatchViewer)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_spectrum = QtWidgets.QAction(BatchViewer)
        self.actionSave_spectrum.setObjectName("actionSave_spectrum")
        self.actionSave_FFT = QtWidgets.QAction(BatchViewer)
        self.actionSave_FFT.setObjectName("actionSave_FFT")
        self.actionCAT = QtWidgets.QAction(BatchViewer)
        self.actionCAT.setObjectName("actionCAT")
        self.actionPeaks = QtWidgets.QAction(BatchViewer)
        self.actionPeaks.setObjectName("actionPeaks")
        self.actionOverlay_settings = QtWidgets.QAction(BatchViewer)
        self.actionOverlay_settings.setObjectName("actionOverlay_settings")
        self.menuFile.addAction(self.actionSave_spectrum)
        self.menuFile.addAction(self.actionSave_FFT)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuLoad_overlay.addAction(self.actionCAT)
        self.menuLoad_overlay.addAction(self.actionPeaks)
        self.menuOverlays.addAction(self.menuLoad_overlay.menuAction())
        self.menuOverlays.addAction(self.actionOverlay_settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOverlays.menuAction())
        self.menubar.addAction(self.menuScan_details.menuAction())

        self.retranslateUi(BatchViewer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BatchViewer)

    def retranslateUi(self, BatchViewer):
        _translate = QtCore.QCoreApplication.translate
        BatchViewer.setWindowTitle(_translate("BatchViewer", "Batch Viewer"))
        self.label_6.setText(_translate("BatchViewer", "FID Processing"))
        self.label_7.setText(_translate("BatchViewer", "Window Function"))
        self.comboBoxWindowFunction.setStatusTip(_translate("BatchViewer", "Apply a window function to the FID."))
        self.comboBoxWindowFunction.setItemText(0, _translate("BatchViewer", "none"))
        self.comboBoxWindowFunction.setItemText(1, _translate("BatchViewer", "blackman"))
        self.comboBoxWindowFunction.setItemText(2, _translate("BatchViewer", "blackmanharris"))
        self.comboBoxWindowFunction.setItemText(3, _translate("BatchViewer", "boxcar"))
        self.comboBoxWindowFunction.setItemText(4, _translate("BatchViewer", "hanning"))
        self.comboBoxWindowFunction.setItemText(5, _translate("BatchViewer", "bartlett"))
        self.label_8.setText(_translate("BatchViewer", "Exponential Filter"))
        self.spinBoxExpFilter.setStatusTip(_translate("BatchViewer", "Apply an exponential filter (microseconds)"))
        self.label_9.setText(_translate("BatchViewer", "High-Pass Filter"))
        self.spinBoxHighPass.setStatusTip(_translate("BatchViewer", "Apply a high-pass filter (microseconds)"))
        self.label_10.setText(_translate("BatchViewer", "Delay"))
        self.spinBoxDelay.setStatusTip(_translate("BatchViewer", "Delay the FID processing (microseconds)"))
        self.spinBoxScanNumber.setToolTip(_translate("BatchViewer", "Select the Scan ID number to display the corresponding FFT."))
        self.label_13.setText(_translate("BatchViewer", "Scan Number"))
        self.spinBoxLowPass.setStatusTip(_translate("BatchViewer", "Apply a high-pass filter (microseconds)"))
        self.label_18.setText(_translate("BatchViewer", "Low-Pass Filter"))
        self.pushButtonReprocess.setText(_translate("BatchViewer", "Reprocess FIDs"))
        self.label_17.setText(_translate("BatchViewer", "DR Processing"))
        self.pushButtonAddRegion.setText(_translate("BatchViewer", "Region"))
        self.pushButtonRemoveRegion.setText(_translate("BatchViewer", "Region"))
        self.label_4.setText(_translate("BatchViewer", "Confine fitting region?"))
        self.checkBoxConfine.setToolTip(_translate("BatchViewer", "Choose whether or not to confine the range to fit the depletion. This is done by moving the region of interest box in the main plot."))
        self.spinBoxSavgolWindow.setToolTip(_translate("BatchViewer", "The window length used for the Savitsky-Golay filter. Must be a positive odd integer."))
        self.label_11.setText(_translate("BatchViewer", "Smoothing Window"))
        self.label_12.setText(_translate("BatchViewer", "Soothing Polynomial"))
        self.spinBoxSavgolPolynomial.setToolTip(_translate("BatchViewer", "The polynomial order used for the Savitsky-Golay filter. Must be an odd, positive integer small than the window length."))
        self.pushButtonFitDR.setToolTip(_translate("BatchViewer", "Fit the DR depletion spectrum using the processing settings above."))
        self.pushButtonFitDR.setText(_translate("BatchViewer", "Fit DR Depletion"))
        self.label_3.setText(_translate("BatchViewer", "DR Frequency"))
        self.labelDRFreq.setStatusTip(_translate("BatchViewer", "Fitted double resonance frequency in MHz. Uncertainty given as one sigma."))
        self.label_5.setText(_translate("BatchViewer", "FWHM"))
        self.labelFWHM.setToolTip(_translate("BatchViewer", "Full-width half maximum for the fitted depletion."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BatchViewer", "Details"))
        self.label.setText(_translate("BatchViewer", "Detection Settings"))
        self.label_16.setText(_translate("BatchViewer", "Detect peaks"))
        self.checkBoxDetectPeaks_3.setStatusTip(_translate("BatchViewer", "Check to automatically detect peaks"))
        self.label_14.setText(_translate("BatchViewer", "Threshold"))
        self.doubleSpinBoxPeakSNRThres_3.setStatusTip(_translate("BatchViewer", "Minimum SNR value for peak detection"))
        self.label_15.setText(_translate("BatchViewer", "Minimum distance"))
        self.doubleSpinBoxPeakMinDist_3.setStatusTip(_translate("BatchViewer", "Minimum distance between detected peaks"))
        self.label_2.setText(_translate("BatchViewer", "Peak Table"))
        self.tableWidgetPeakTable.setStatusTip(_translate("BatchViewer", "Table of detected peaks in the spectrum"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BatchViewer", "Peaks"))
        self.menuFile.setTitle(_translate("BatchViewer", "File"))
        self.menuOverlays.setTitle(_translate("BatchViewer", "Overlays"))
        self.menuLoad_overlay.setTitle(_translate("BatchViewer", "Load overlay..."))
        self.menuScan_details.setTitle(_translate("BatchViewer", "Scan details"))
        self.actionClose.setText(_translate("BatchViewer", "Close"))
        self.actionSave_spectrum.setText(_translate("BatchViewer", "Save spectrum"))
        self.actionSave_FFT.setText(_translate("BatchViewer", "Save FFT"))
        self.actionCAT.setText(_translate("BatchViewer", "CAT"))
        self.actionPeaks.setText(_translate("BatchViewer", "Peaks"))
        self.actionOverlay_settings.setText(_translate("BatchViewer", "Overlay settings"))

from pyqtgraph import GraphicsLayoutWidget
import icons_rc
