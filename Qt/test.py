# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 141, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.testButton.setObjectName("testButton")
        self.verticalLayout.addWidget(self.testButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.amplitudeEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.amplitudeEdit_2.setMaximumSize(QtCore.QSize(70, 40))
        self.amplitudeEdit_2.setObjectName("amplitudeEdit_2")
        self.horizontalLayout_2.addWidget(self.amplitudeEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.amplitudeEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.amplitudeEdit.setMaximumSize(QtCore.QSize(70, 40))
        self.amplitudeEdit.setObjectName("amplitudeEdit")
        self.horizontalLayout.addWidget(self.amplitudeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 60, 711, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_spectrum = QtWidgets.QAction(MainWindow)
        self.actionLoad_spectrum.setObjectName("actionLoad_spectrum")
        self.actionSave_spectrum = QtWidgets.QAction(MainWindow)
        self.actionSave_spectrum.setObjectName("actionSave_spectrum")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_spectrum)
        self.menuFile.addAction(self.actionSave_spectrum)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "Amplitude"))
        self.label.setText(_translate("MainWindow", "Amplitude"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_spectrum.setText(_translate("MainWindow", "Load spectrum"))
        self.actionSave_spectrum.setText(_translate("MainWindow", "Save spectrum"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

