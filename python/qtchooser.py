# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt/ScanChooser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScanChooser(object):
    def setupUi(self, ScanChooser):
        ScanChooser.setObjectName("ScanChooser")
        ScanChooser.resize(352, 551)
        ScanChooser.setMinimumSize(QtCore.QSize(352, 551))
        ScanChooser.setMaximumSize(QtCore.QSize(352, 551))
        ScanChooser.setStyleSheet("QMainWindow {\n"
" background-color: #ffffff\n"
"}\n"
"\n"
"QMenuBar {\n"
" background-color: #ffffff;\n"
" color: #ffffff\n"
"}\n"
"\n"
"QMenuBar::item {\n"
" background: transparent;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" background: #E37222\n"
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
"color: #2c7fb8\n"
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
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #edf8b1;\n"
"color: #2c7fb8\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #edf8b1;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QPushButton {\n"
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
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(ScanChooser)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxScanChooser = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxScanChooser.setObjectName("comboBoxScanChooser")
        self.comboBoxScanChooser.addItem("")
        self.comboBoxScanChooser.addItem("")
        self.comboBoxScanChooser.addItem("")
        self.verticalLayout.addWidget(self.comboBoxScanChooser)
        self.tableWidgetScanChooser = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidgetScanChooser.setFont(font)
        self.tableWidgetScanChooser.setObjectName("tableWidgetScanChooser")
        self.tableWidgetScanChooser.setColumnCount(0)
        self.tableWidgetScanChooser.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidgetScanChooser)
        self.spinBoxBatchNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxBatchNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBoxBatchNumber.setMaximum(10000000)
        self.spinBoxBatchNumber.setObjectName("spinBoxBatchNumber")
        self.verticalLayout.addWidget(self.spinBoxBatchNumber)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxWindowFunction = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxWindowFunction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxWindowFunction.setObjectName("comboBoxWindowFunction")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.comboBoxWindowFunction.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxWindowFunction)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBoxExpFilter = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxExpFilter.setToolTip("")
        self.spinBoxExpFilter.setToolTipDuration(2)
        self.spinBoxExpFilter.setMaximum(1000)
        self.spinBoxExpFilter.setSingleStep(10)
        self.spinBoxExpFilter.setObjectName("spinBoxExpFilter")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxExpFilter)
        self.spinBoxHighPass = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxHighPass.setMaximum(1000)
        self.spinBoxHighPass.setObjectName("spinBoxHighPass")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxHighPass)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.spinBoxDelay = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBoxDelay.setSuffix("")
        self.spinBoxDelay.setMaximum(1000)
        self.spinBoxDelay.setObjectName("spinBoxDelay")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxDelay)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonCloseChooser = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonCloseChooser.setObjectName("pushButtonCloseChooser")
        self.horizontalLayout.addWidget(self.pushButtonCloseChooser)
        self.pushButtonOpenScan = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonOpenScan.setObjectName("pushButtonOpenScan")
        self.horizontalLayout.addWidget(self.pushButtonOpenScan)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_9.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(ScanChooser)
        QtCore.QMetaObject.connectSlotsByName(ScanChooser)

    def retranslateUi(self, ScanChooser):
        _translate = QtCore.QCoreApplication.translate
        ScanChooser.setWindowTitle(_translate("ScanChooser", "Scan Chooser"))
        self.comboBoxScanChooser.setItemText(0, _translate("ScanChooser", "Survey"))
        self.comboBoxScanChooser.setItemText(1, _translate("ScanChooser", "Batch"))
        self.comboBoxScanChooser.setItemText(2, _translate("ScanChooser", "DR Batch"))
        self.tableWidgetScanChooser.setToolTip(_translate("ScanChooser", "Specify the scan/batch number"))
        self.spinBoxBatchNumber.setToolTip(_translate("ScanChooser", "Specify the batch/scan number"))
        self.label_5.setText(_translate("ScanChooser", "FID Processing"))
        self.label_7.setText(_translate("ScanChooser", "Window Function"))
        self.comboBoxWindowFunction.setStatusTip(_translate("ScanChooser", "Apply a window function to the FID."))
        self.comboBoxWindowFunction.setItemText(0, _translate("ScanChooser", "none"))
        self.comboBoxWindowFunction.setItemText(1, _translate("ScanChooser", "blackman"))
        self.comboBoxWindowFunction.setItemText(2, _translate("ScanChooser", "blackmanharris"))
        self.comboBoxWindowFunction.setItemText(3, _translate("ScanChooser", "boxcar"))
        self.comboBoxWindowFunction.setItemText(4, _translate("ScanChooser", "hanning"))
        self.comboBoxWindowFunction.setItemText(5, _translate("ScanChooser", "bartlett"))
        self.label_8.setText(_translate("ScanChooser", "Exponential Filter"))
        self.spinBoxExpFilter.setStatusTip(_translate("ScanChooser", "Apply an exponential filter (microseconds)"))
        self.spinBoxHighPass.setStatusTip(_translate("ScanChooser", "Apply a high-pass filter (microseconds)"))
        self.label_10.setText(_translate("ScanChooser", "Delay"))
        self.spinBoxDelay.setStatusTip(_translate("ScanChooser", "Delay the FID processing (microseconds)"))
        self.label_9.setText(_translate("ScanChooser", "High-Pass Filter"))
        self.pushButtonCloseChooser.setText(_translate("ScanChooser", "Close"))
        self.pushButtonOpenScan.setText(_translate("ScanChooser", "Open"))

