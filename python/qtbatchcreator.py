# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatchCreator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchCreator(object):
    def setupUi(self, BatchCreator):
        BatchCreator.setObjectName("BatchCreator")
        BatchCreator.resize(870, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchCreator.sizePolicy().hasHeightForWidth())
        BatchCreator.setSizePolicy(sizePolicy)
        BatchCreator.setMinimumSize(QtCore.QSize(870, 720))
        BatchCreator.setMaximumSize(QtCore.QSize(870, 720))
        BatchCreator.setStyleSheet("QMainWindow {\n"
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
"QToolButton {\n"
" background-color: #FFFFFF;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border: 1.5px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"min-width: 5ex;\n"
"padding: 2px;\n"
"font-family: \'Roboto\', sans-serif;\n"
"font-weight: 500;\n"
"font-size: 15px;\n"
"color: #2c7fb8;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #FFFFFF;\n"
"    color: #2c7fb8;\n"
"    font-size: 12px;\n"
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
"font-family: \'Roboto\', sans-serif;\n"
"font-size: 15px\n"
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
"}")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(BatchCreator)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(12, 12, 848, 672))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.tableWidgetChosenScans = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidgetChosenScans.setFont(font)
        self.tableWidgetChosenScans.setColumnCount(1)
        self.tableWidgetChosenScans.setObjectName("tableWidgetChosenScans")
        self.tableWidgetChosenScans.setRowCount(0)
        self.tableWidgetChosenScans.horizontalHeader().setVisible(False)
        self.tableWidgetChosenScans.horizontalHeader().setHighlightSections(True)
        self.verticalLayout_2.addWidget(self.tableWidgetChosenScans)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.tableWidgetChosenCal = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidgetChosenCal.setFont(font)
        self.tableWidgetChosenCal.setColumnCount(1)
        self.tableWidgetChosenCal.setObjectName("tableWidgetChosenCal")
        self.tableWidgetChosenCal.setRowCount(0)
        self.tableWidgetChosenCal.horizontalHeader().setVisible(False)
        self.tableWidgetChosenCal.horizontalHeader().setHighlightSections(True)
        self.verticalLayout_2.addWidget(self.tableWidgetChosenCal)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.checkBoxFilter = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBoxFilter.setText("")
        self.checkBoxFilter.setObjectName("checkBoxFilter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBoxFilter)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBoxSearchFreq = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxSearchFreq.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxSearchFreq.setSizePolicy(sizePolicy)
        self.doubleSpinBoxSearchFreq.setMinimumSize(QtCore.QSize(88, 0))
        self.doubleSpinBoxSearchFreq.setSuffix("")
        self.doubleSpinBoxSearchFreq.setDecimals(3)
        self.doubleSpinBoxSearchFreq.setMaximum(100000.0)
        self.doubleSpinBoxSearchFreq.setObjectName("doubleSpinBoxSearchFreq")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxSearchFreq)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.calendarWidgetStartDate = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidgetStartDate.sizePolicy().hasHeightForWidth())
        self.calendarWidgetStartDate.setSizePolicy(sizePolicy)
        self.calendarWidgetStartDate.setMinimumSize(QtCore.QSize(0, 0))
        self.calendarWidgetStartDate.setMaximumSize(QtCore.QSize(250, 400))
        self.calendarWidgetStartDate.setSelectedDate(QtCore.QDate(2010, 1, 1))
        self.calendarWidgetStartDate.setGridVisible(True)
        self.calendarWidgetStartDate.setObjectName("calendarWidgetStartDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.calendarWidgetStartDate)
        self.calendarWidgetEndDate = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidgetEndDate.sizePolicy().hasHeightForWidth())
        self.calendarWidgetEndDate.setSizePolicy(sizePolicy)
        self.calendarWidgetEndDate.setMinimumSize(QtCore.QSize(0, 0))
        self.calendarWidgetEndDate.setMaximumSize(QtCore.QSize(250, 400))
        self.calendarWidgetEndDate.setGridVisible(True)
        self.calendarWidgetEndDate.setObjectName("calendarWidgetEndDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.calendarWidgetEndDate)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_2)
        self.pushButtonRemoveScans = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRemoveScans.setIcon(icon)
        self.pushButtonRemoveScans.setObjectName("pushButtonRemoveScans")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.pushButtonRemoveScans)
        self.pushButtonAddScans = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/plus-8x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddScans.setIcon(icon1)
        self.pushButtonAddScans.setObjectName("pushButtonAddScans")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButtonAddScans)
        self.pushButtonRemoveCal = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonRemoveCal.setIcon(icon)
        self.pushButtonRemoveCal.setObjectName("pushButtonRemoveCal")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButtonRemoveCal)
        self.pushButtonAddCal = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonAddCal.setIcon(icon1)
        self.pushButtonAddCal.setObjectName("pushButtonAddCal")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButtonAddCal)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBoxBatchStart = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxBatchStart.sizePolicy().hasHeightForWidth())
        self.spinBoxBatchStart.setSizePolicy(sizePolicy)
        self.spinBoxBatchStart.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxBatchStart.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBoxBatchStart.setMaximum(10000000)
        self.spinBoxBatchStart.setObjectName("spinBoxBatchStart")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.spinBoxBatchStart)
        self.spinBoxBatchEnd = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxBatchEnd.sizePolicy().hasHeightForWidth())
        self.spinBoxBatchEnd.setSizePolicy(sizePolicy)
        self.spinBoxBatchEnd.setMinimumSize(QtCore.QSize(88, 0))
        self.spinBoxBatchEnd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBoxBatchEnd.setMaximum(10000000)
        self.spinBoxBatchEnd.setObjectName("spinBoxBatchEnd")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spinBoxBatchEnd)
        self.pushButtonRemoveRange = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonRemoveRange.setIcon(icon)
        self.pushButtonRemoveRange.setObjectName("pushButtonRemoveRange")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButtonRemoveRange)
        self.pushButtonAddRange = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonAddRange.setIcon(icon1)
        self.pushButtonAddRange.setObjectName("pushButtonAddRange")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pushButtonAddRange)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonCloseChooser = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonCloseChooser.setObjectName("pushButtonCloseChooser")
        self.horizontalLayout.addWidget(self.pushButtonCloseChooser)
        self.pushButtonOpenScan = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonOpenScan.setObjectName("pushButtonOpenScan")
        self.horizontalLayout.addWidget(self.pushButtonOpenScan)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tableWidgetScanChooser = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidgetScanChooser.setFont(font)
        self.tableWidgetScanChooser.setColumnCount(1)
        self.tableWidgetScanChooser.setObjectName("tableWidgetScanChooser")
        self.tableWidgetScanChooser.setRowCount(0)
        self.tableWidgetScanChooser.horizontalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.tableWidgetScanChooser)

        self.retranslateUi(BatchCreator)
        QtCore.QMetaObject.connectSlotsByName(BatchCreator)

    def retranslateUi(self, BatchCreator):
        _translate = QtCore.QCoreApplication.translate
        BatchCreator.setWindowTitle(_translate("BatchCreator", "Batch Creator"))
        self.label_7.setText(_translate("BatchCreator", "Batch Scans"))
        self.tableWidgetChosenScans.setToolTip(_translate("BatchCreator", "Scan numbers to be added to the created batch."))
        self.label_5.setText(_translate("BatchCreator", "Calibration Scans"))
        self.tableWidgetChosenCal.setToolTip(_translate("BatchCreator", "Scan numbers to be added to the created batch."))
        self.label_6.setText(_translate("BatchCreator", "Filter search?"))
        self.checkBoxFilter.setToolTip(_translate("BatchCreator", "Choose whether to filter the results based on the conditions below."))
        self.label_2.setText(_translate("BatchCreator", "Search Frequency"))
        self.doubleSpinBoxSearchFreq.setToolTip(_translate("BatchCreator", "Frequency to search for in MHz."))
        self.label_4.setText(_translate("BatchCreator", "Start Search Date"))
        self.label_3.setText(_translate("BatchCreator", "End Search Date"))
        self.calendarWidgetStartDate.setToolTip(_translate("BatchCreator", "Start Date"))
        self.pushButtonRemoveScans.setText(_translate("BatchCreator", "Remove Scans"))
        self.pushButtonAddScans.setText(_translate("BatchCreator", "Add Scans"))
        self.pushButtonRemoveCal.setText(_translate("BatchCreator", "Remove Calibration"))
        self.pushButtonAddCal.setText(_translate("BatchCreator", "Add Calibration"))
        self.label_8.setText(_translate("BatchCreator", "Select ID Range"))
        self.spinBoxBatchStart.setToolTip(_translate("BatchCreator", "Specify the batch/scan number"))
        self.spinBoxBatchEnd.setToolTip(_translate("BatchCreator", "Specify the batch/scan number"))
        self.pushButtonRemoveRange.setText(_translate("BatchCreator", "Remove Range"))
        self.pushButtonAddRange.setText(_translate("BatchCreator", "Add Range"))
        self.pushButtonCloseChooser.setText(_translate("BatchCreator", "Close"))
        self.pushButtonOpenScan.setText(_translate("BatchCreator", "Open"))
        self.tableWidgetScanChooser.setToolTip(_translate("BatchCreator", "Lists the scan numbers that satisfy the search conditions."))

import icons_rc
