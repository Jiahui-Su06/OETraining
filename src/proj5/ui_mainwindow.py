# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolBar, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 702)
        icon = QIcon()
        icon.addFile(u":/logo/images/proj4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSave.setIcon(icon2)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionClose.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon()
        icon4.addFile(u":/logo/images/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon4)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon5 = QIcon()
        icon5.addFile(u":/logo/images/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon5)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon6 = QIcon()
        icon6.addFile(u":/logo/images/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon6)
        self.actionRecord = QAction(MainWindow)
        self.actionRecord.setObjectName(u"actionRecord")
        icon7 = QIcon()
        icon7.addFile(u":/logo/images/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRecord.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.groupBox_6)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(120, 16777215))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.groupBox_5)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMinimumSize(QSize(700, 550))

        self.verticalLayout_6.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.portBox = QComboBox(self.groupBox_2)
        self.portBox.setObjectName(u"portBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.portBox.sizePolicy().hasHeightForWidth())
        self.portBox.setSizePolicy(sizePolicy3)
        self.portBox.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.portBox, 0, 1, 1, 1)

        self.refreshBtn = QPushButton(self.groupBox_2)
        self.refreshBtn.setObjectName(u"refreshBtn")

        self.gridLayout.addWidget(self.refreshBtn, 1, 0, 1, 1)

        self.openBtn = QPushButton(self.groupBox_2)
        self.openBtn.setObjectName(u"openBtn")

        self.gridLayout.addWidget(self.openBtn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.setBtn = QPushButton(self.groupBox_3)
        self.setBtn.setObjectName(u"setBtn")

        self.gridLayout_2.addWidget(self.setBtn, 2, 0, 1, 1)

        self.readBtn = QPushButton(self.groupBox_3)
        self.readBtn.setObjectName(u"readBtn")

        self.gridLayout_2.addWidget(self.readBtn, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.timeBox = QSpinBox(self.groupBox_3)
        self.timeBox.setObjectName(u"timeBox")
        self.timeBox.setMaximumSize(QSize(120, 16777215))
        self.timeBox.setMinimum(1)
        self.timeBox.setMaximum(100)

        self.gridLayout_2.addWidget(self.timeBox, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.x1Edit = QLineEdit(self.groupBox_4)
        self.x1Edit.setObjectName(u"x1Edit")
        sizePolicy3.setHeightForWidth(self.x1Edit.sizePolicy().hasHeightForWidth())
        self.x1Edit.setSizePolicy(sizePolicy3)
        self.x1Edit.setMaximumSize(QSize(60, 16777215))
        self.x1Edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.x1Edit, 1, 1, 1, 1)

        self.intervalBox = QComboBox(self.groupBox_4)
        self.intervalBox.setObjectName(u"intervalBox")
        sizePolicy3.setHeightForWidth(self.intervalBox.sizePolicy().hasHeightForWidth())
        self.intervalBox.setSizePolicy(sizePolicy3)
        self.intervalBox.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.intervalBox, 3, 2, 1, 2)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)

        self.meanEdit = QLineEdit(self.groupBox_4)
        self.meanEdit.setObjectName(u"meanEdit")
        sizePolicy3.setHeightForWidth(self.meanEdit.sizePolicy().hasHeightForWidth())
        self.meanEdit.setSizePolicy(sizePolicy3)
        self.meanEdit.setMaximumSize(QSize(60, 16777215))
        self.meanEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.meanEdit, 5, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_5, 2, 2, 1, 1)

        self.xEdit = QLineEdit(self.groupBox_4)
        self.xEdit.setObjectName(u"xEdit")
        sizePolicy3.setHeightForWidth(self.xEdit.sizePolicy().hasHeightForWidth())
        self.xEdit.setSizePolicy(sizePolicy3)
        self.xEdit.setMaximumSize(QSize(60, 16777215))
        self.xEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.xEdit, 2, 1, 1, 1)

        self.LEdit = QLineEdit(self.groupBox_4)
        self.LEdit.setObjectName(u"LEdit")
        sizePolicy3.setHeightForWidth(self.LEdit.sizePolicy().hasHeightForWidth())
        self.LEdit.setSizePolicy(sizePolicy3)
        self.LEdit.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.LEdit, 4, 1, 1, 1)

        self.thrEdit = QLineEdit(self.groupBox_4)
        self.thrEdit.setObjectName(u"thrEdit")
        sizePolicy3.setHeightForWidth(self.thrEdit.sizePolicy().hasHeightForWidth())
        self.thrEdit.setSizePolicy(sizePolicy3)
        self.thrEdit.setMaximumSize(QSize(60, 16777215))
        self.thrEdit.setReadOnly(False)

        self.gridLayout_3.addWidget(self.thrEdit, 2, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.x2Edit = QLineEdit(self.groupBox_4)
        self.x2Edit.setObjectName(u"x2Edit")
        sizePolicy3.setHeightForWidth(self.x2Edit.sizePolicy().hasHeightForWidth())
        self.x2Edit.setSizePolicy(sizePolicy3)
        self.x2Edit.setMaximumSize(QSize(60, 16777215))
        self.x2Edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.x2Edit, 1, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.RMSEdit = QLineEdit(self.groupBox_4)
        self.RMSEdit.setObjectName(u"RMSEdit")
        sizePolicy3.setHeightForWidth(self.RMSEdit.sizePolicy().hasHeightForWidth())
        self.RMSEdit.setSizePolicy(sizePolicy3)
        self.RMSEdit.setMaximumSize(QSize(60, 16777215))
        self.RMSEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.RMSEdit, 5, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.DEdit = QLineEdit(self.groupBox_4)
        self.DEdit.setObjectName(u"DEdit")
        sizePolicy3.setHeightForWidth(self.DEdit.sizePolicy().hasHeightForWidth())
        self.DEdit.setSizePolicy(sizePolicy3)
        self.DEdit.setMaximumSize(QSize(60, 16777215))
        self.DEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.DEdit, 4, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_9, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.label_6, 4, 2, 1, 1)

        self.deleteBtn = QPushButton(self.groupBox_4)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.deleteBtn, 7, 0, 1, 2)

        self.clearBtn = QPushButton(self.groupBox_4)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.clearBtn, 7, 2, 1, 2)

        self.saveBtn = QPushButton(self.groupBox_4)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.saveBtn, 6, 2, 1, 2)

        self.recordBtn = QPushButton(self.groupBox_4)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_3.addWidget(self.recordBtn, 6, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.textBrowser)


        self.verticalLayout_5.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionRecord)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRecord)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Laser Diffraction Measurement System", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRecord.setText(QCoreApplication.translate("MainWindow", u"Record Data", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Collected Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"D (mm)", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"CCD Data", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Serial Port Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port (FTDI):", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh Device", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"Open Device", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"CCD Settings", None))
        self.setBtn.setText(QCoreApplication.translate("MainWindow", u"Set Integration", None))
        self.readBtn.setText(QCoreApplication.translate("MainWindow", u"Read CCD", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Integral Time (ms):", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X2 (pixel):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"L (mm):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.LEdit.setText(QCoreApplication.translate("MainWindow", u"670", None))
        self.thrEdit.setText(QCoreApplication.translate("MainWindow", u"45000", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mean:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X1 (pixel):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Interval Time (s):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0394X (pixel):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"RMS:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"D (mm):", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.recordBtn.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File(&F)", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit(&E)", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help(&H)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

