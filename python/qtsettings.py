# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt/Settings.ui'
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
" background-color: #d9d9d9\n"
"}\n"
"\n"
"QMenuBar {\n"
" background-color: #66B9BF;\n"
" color: #d9d9d9\n"
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
" background-color: #d9d9d9\n"
"}\n"
"\n"
"QTabWidget {\n"
"background-color: #66B9BF\n"
"}\n"
"\n"
"QLabel {\n"
"color: #07889B\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"    background-color: #EEAA7B;\n"
"    color: #d9d9d9;\n"
"    font-size: 15px;\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: #EEAA7B;\n"
"    color: #d9d9d9;\n"
"    font-size: 15px;\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: #EEAA7B;\n"
"color: #d9d9d9;\n"
"font-size: 15px;\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
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
"background: #EEAA7B;\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #E37222;\n"
"color: #d9d9d9\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.frame = QtWidgets.QFrame(SettingsForm)
        self.frame.setGeometry(QtCore.QRect(12, 12, 616, 456))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 351))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
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
        self.commandLinkButtonQTFTMPath = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commandLinkButtonQTFTMPath.setFont(font)
        self.commandLinkButtonQTFTMPath.setWhatsThis("")
        self.commandLinkButtonQTFTMPath.setObjectName("commandLinkButtonQTFTMPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commandLinkButtonQTFTMPath)
        self.commandLinkButtonChirpPath = QtWidgets.QCommandLinkButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commandLinkButtonChirpPath.setFont(font)
        self.commandLinkButtonChirpPath.setWhatsThis("")
        self.commandLinkButtonChirpPath.setObjectName("commandLinkButtonChirpPath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commandLinkButtonChirpPath)
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
        self.label_2.setText(_translate("SettingsForm", "Chirp Data Path"))
        self.lineEditChirpPath.setToolTip(_translate("SettingsForm", "The path to the root of blackchirp"))
        self.commandLinkButtonQTFTMPath.setToolTip(_translate("SettingsForm", "Open a file directory browser to locate chirp path"))
        self.commandLinkButtonQTFTMPath.setText(_translate("SettingsForm", "Locate"))
        self.commandLinkButtonChirpPath.setToolTip(_translate("SettingsForm", "Open a file directory browser to locate chirp path"))
        self.commandLinkButtonChirpPath.setText(_translate("SettingsForm", "Locate"))
        self.pushButtonCloseSettings.setText(_translate("SettingsForm", "Close"))
        self.pushButtonSaveSettings.setText(_translate("SettingsForm", "Save Settings"))

