# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsForm(object):
    def setupUi(self, SettingsForm):
        SettingsForm.setObjectName("SettingsForm")
        SettingsForm.resize(640, 480)
        SettingsForm.setStyleSheet("QMainWindow {\n"
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
        self.frame = QtWidgets.QFrame(SettingsForm)
        self.frame.setGeometry(QtCore.QRect(12, 12, 616, 456))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 867, 434))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditQtFTMPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditQtFTMPath.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEditQtFTMPath.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditQtFTMPath.setFont(font)
        self.lineEditQtFTMPath.setText("")
        self.lineEditQtFTMPath.setObjectName("lineEditQtFTMPath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditQtFTMPath)
        self.commandLinkButtonQTFTMPath = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.commandLinkButtonQTFTMPath.setFont(font)
        self.commandLinkButtonQTFTMPath.setWhatsThis("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/magnifying-glass-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButtonQTFTMPath.setIcon(icon)
        self.commandLinkButtonQTFTMPath.setObjectName("commandLinkButtonQTFTMPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commandLinkButtonQTFTMPath)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditChirpPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditChirpPath.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEditChirpPath.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditChirpPath.setFont(font)
        self.lineEditChirpPath.setText("")
        self.lineEditChirpPath.setObjectName("lineEditChirpPath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditChirpPath)
        self.commandLinkButtonChirpPath = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.commandLinkButtonChirpPath.setFont(font)
        self.commandLinkButtonChirpPath.setWhatsThis("")
        self.commandLinkButtonChirpPath.setIcon(icon)
        self.commandLinkButtonChirpPath.setObjectName("commandLinkButtonChirpPath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commandLinkButtonChirpPath)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.checkBoxUseHDF5 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBoxUseHDF5.setText("")
        self.checkBoxUseHDF5.setObjectName("checkBoxUseHDF5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBoxUseHDF5)
        self.lineEditHDF5Path = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditHDF5Path.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEditHDF5Path.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditHDF5Path.setFont(font)
        self.lineEditHDF5Path.setText("")
        self.lineEditHDF5Path.setObjectName("lineEditHDF5Path")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditHDF5Path)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.commandLinkButtonHDFPath = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.commandLinkButtonHDFPath.setFont(font)
        self.commandLinkButtonHDFPath.setWhatsThis("")
        self.commandLinkButtonHDFPath.setIcon(icon)
        self.commandLinkButtonHDFPath.setObjectName("commandLinkButtonHDFPath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commandLinkButtonHDFPath)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 601, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonCloseSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCloseSettings.setObjectName("pushButtonCloseSettings")
        self.horizontalLayout.addWidget(self.pushButtonCloseSettings)
        self.pushButtonSaveSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSaveSettings.setObjectName("pushButtonSaveSettings")
        self.horizontalLayout.addWidget(self.pushButtonSaveSettings)

        self.retranslateUi(SettingsForm)
        QtCore.QMetaObject.connectSlotsByName(SettingsForm)

    def retranslateUi(self, SettingsForm):
        _translate = QtCore.QCoreApplication.translate
        SettingsForm.setWindowTitle(_translate("SettingsForm", "Form"))
        self.label.setText(_translate("SettingsForm", "QtFTM Data Path"))
        self.lineEditQtFTMPath.setToolTip(_translate("SettingsForm", "The path to the root of QtFTM"))
        self.commandLinkButtonQTFTMPath.setToolTip(_translate("SettingsForm", "Open a file directory browser to locate chirp path"))
        self.commandLinkButtonQTFTMPath.setText(_translate("SettingsForm", "Locate"))
        self.label_2.setText(_translate("SettingsForm", "Chirp Data Path"))
        self.lineEditChirpPath.setToolTip(_translate("SettingsForm", "The path to the root of blackchirp"))
        self.commandLinkButtonChirpPath.setToolTip(_translate("SettingsForm", "Open a file directory browser to locate chirp path"))
        self.commandLinkButtonChirpPath.setText(_translate("SettingsForm", "Locate"))
        self.label_3.setText(_translate("SettingsForm", "Use HDF5 Database?"))
        self.lineEditHDF5Path.setToolTip(_translate("SettingsForm", "The path to the root of blackchirp"))
        self.label_10.setText(_translate("SettingsForm", "HDF5 Path"))
        self.commandLinkButtonHDFPath.setToolTip(_translate("SettingsForm", "Open a file directory browser to locate chirp path"))
        self.commandLinkButtonHDFPath.setText(_translate("SettingsForm", "Locate"))
        self.pushButtonCloseSettings.setText(_translate("SettingsForm", "Close"))
        self.pushButtonSaveSettings.setText(_translate("SettingsForm", "Save Settings"))

import icons_rc
