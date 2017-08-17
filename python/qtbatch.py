# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt/BatchViewer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchViewer(object):
    def setupUi(self, BatchViewer):
        BatchViewer.setObjectName("BatchViewer")
        BatchViewer.resize(1083, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchViewer.sizePolicy().hasHeightForWidth())
        BatchViewer.setSizePolicy(sizePolicy)
        BatchViewer.setStyleSheet("QMainWindow {\n"
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
" color: #2c7fb8;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" background: #edf8b1;\n"
" color: #2c7fb8\n"
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
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

        self.retranslateUi(BatchViewer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BatchViewer)

    def retranslateUi(self, BatchViewer):
        _translate = QtCore.QCoreApplication.translate
        BatchViewer.setWindowTitle(_translate("BatchViewer", "Batch Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BatchViewer", "FID Processing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BatchViewer", "Peaks"))
        self.menuFile.setTitle(_translate("BatchViewer", "File"))
        self.menuOverlays.setTitle(_translate("BatchViewer", "Overlays"))
        self.menuLoad_overlay.setTitle(_translate("BatchViewer", "Load overlay..."))
        self.actionClose.setText(_translate("BatchViewer", "Close"))
        self.actionSave_spectrum.setText(_translate("BatchViewer", "Save spectrum"))
        self.actionSave_FFT.setText(_translate("BatchViewer", "Save FFT"))
        self.actionCAT.setText(_translate("BatchViewer", "CAT"))
        self.actionPeaks.setText(_translate("BatchViewer", "Peaks"))
        self.actionOverlay_settings.setText(_translate("BatchViewer", "Overlay settings"))

from pyqtgraph import GraphicsLayoutWidget
