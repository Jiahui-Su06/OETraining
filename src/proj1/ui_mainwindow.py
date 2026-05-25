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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1098, 642)
        icon = QIcon()
        icon.addFile(u":/logo/images/proj1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSave.setIcon(icon1)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon2)
        self.actionAnalysis = QAction(MainWindow)
        self.actionAnalysis.setObjectName(u"actionAnalysis")
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/analysis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAnalysis.setIcon(icon3)
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
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon6 = QIcon()
        icon6.addFile(u":/logo/images/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen.setIcon(icon6)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon7 = QIcon()
        icon7.addFile(u":/logo/images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionClear.setIcon(icon7)
        self.actionRecord = QAction(MainWindow)
        self.actionRecord.setObjectName(u"actionRecord")
        icon8 = QIcon()
        icon8.addFile(u":/logo/images/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRecord.setIcon(icon8)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon9 = QIcon()
        icon9.addFile(u":/logo/images/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDelete.setIcon(icon9)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon10 = QIcon()
        icon10.addFile(u":/logo/images/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionClose.setIcon(icon10)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.groupBox_5)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMaximumSize(QSize(230, 16777215))
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView = QGraphicsView(self.groupBox_4)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy2)
        self.graphicsView.setMinimumSize(QSize(500, 500))

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.portComboBox = QComboBox(self.groupBox)
        self.portComboBox.setObjectName(u"portComboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.portComboBox.sizePolicy().hasHeightForWidth())
        self.portComboBox.setSizePolicy(sizePolicy4)
        self.portComboBox.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.portComboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.resistanceBox = QSpinBox(self.groupBox)
        self.resistanceBox.setObjectName(u"resistanceBox")
        self.resistanceBox.setMaximumSize(QSize(80, 16777215))
        self.resistanceBox.setMinimum(1)
        self.resistanceBox.setMaximum(31)
        self.resistanceBox.setValue(1)

        self.gridLayout.addWidget(self.resistanceBox, 0, 3, 1, 1)

        self.connectBtn = QPushButton(self.groupBox)
        self.connectBtn.setObjectName(u"connectBtn")
        sizePolicy4.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy4)
        self.connectBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.connectBtn, 1, 0, 1, 2)

        self.setResistanceBtn = QPushButton(self.groupBox)
        self.setResistanceBtn.setObjectName(u"setResistanceBtn")
        self.setResistanceBtn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.setResistanceBtn, 1, 2, 1, 2)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.xPosEdit = QLineEdit(self.groupBox_2)
        self.xPosEdit.setObjectName(u"xPosEdit")
        sizePolicy4.setHeightForWidth(self.xPosEdit.sizePolicy().hasHeightForWidth())
        self.xPosEdit.setSizePolicy(sizePolicy4)
        self.xPosEdit.setMaximumSize(QSize(80, 16777215))
        self.xPosEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.xPosEdit, 3, 1, 1, 1)

        self.v00Edit = QLineEdit(self.groupBox_2)
        self.v00Edit.setObjectName(u"v00Edit")
        sizePolicy4.setHeightForWidth(self.v00Edit.sizePolicy().hasHeightForWidth())
        self.v00Edit.setSizePolicy(sizePolicy4)
        self.v00Edit.setMaximumSize(QSize(80, 16777215))
        self.v00Edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.v00Edit, 0, 1, 1, 1)

        self.moveEdit = QLineEdit(self.groupBox_2)
        self.moveEdit.setObjectName(u"moveEdit")
        sizePolicy4.setHeightForWidth(self.moveEdit.sizePolicy().hasHeightForWidth())
        self.moveEdit.setSizePolicy(sizePolicy4)
        self.moveEdit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.moveEdit, 4, 1, 1, 1)

        self.v10Edit = QLineEdit(self.groupBox_2)
        self.v10Edit.setObjectName(u"v10Edit")
        sizePolicy4.setHeightForWidth(self.v10Edit.sizePolicy().hasHeightForWidth())
        self.v10Edit.setSizePolicy(sizePolicy4)
        self.v10Edit.setMaximumSize(QSize(80, 16777215))
        self.v10Edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.v10Edit, 1, 1, 1, 1)

        self.pxEdit = QLineEdit(self.groupBox_2)
        self.pxEdit.setObjectName(u"pxEdit")
        sizePolicy4.setHeightForWidth(self.pxEdit.sizePolicy().hasHeightForWidth())
        self.pxEdit.setSizePolicy(sizePolicy4)
        self.pxEdit.setMaximumSize(QSize(80, 16777215))
        self.pxEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.pxEdit, 2, 1, 1, 1)

        self.v11Edit = QLineEdit(self.groupBox_2)
        self.v11Edit.setObjectName(u"v11Edit")
        sizePolicy4.setHeightForWidth(self.v11Edit.sizePolicy().hasHeightForWidth())
        self.v11Edit.setSizePolicy(sizePolicy4)
        self.v11Edit.setMaximumSize(QSize(80, 16777215))
        self.v11Edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.v11Edit, 1, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.v01Edit = QLineEdit(self.groupBox_2)
        self.v01Edit.setObjectName(u"v01Edit")
        sizePolicy4.setHeightForWidth(self.v01Edit.sizePolicy().hasHeightForWidth())
        self.v01Edit.setSizePolicy(sizePolicy4)
        self.v01Edit.setMaximumSize(QSize(80, 16777215))
        self.v01Edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.v01Edit, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setTabletTracking(False)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.deleteBtn = QPushButton(self.groupBox_2)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.gridLayout_2.addWidget(self.deleteBtn, 5, 2, 1, 2)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.pyEdit = QLineEdit(self.groupBox_2)
        self.pyEdit.setObjectName(u"pyEdit")
        sizePolicy4.setHeightForWidth(self.pyEdit.sizePolicy().hasHeightForWidth())
        self.pyEdit.setSizePolicy(sizePolicy4)
        self.pyEdit.setMaximumSize(QSize(80, 16777215))
        self.pyEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.pyEdit, 2, 3, 1, 1)

        self.yPosEdit = QLineEdit(self.groupBox_2)
        self.yPosEdit.setObjectName(u"yPosEdit")
        sizePolicy4.setHeightForWidth(self.yPosEdit.sizePolicy().hasHeightForWidth())
        self.yPosEdit.setSizePolicy(sizePolicy4)
        self.yPosEdit.setMaximumSize(QSize(80, 16777215))
        self.yPosEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.yPosEdit, 3, 3, 1, 1)

        self.clearBtn = QPushButton(self.groupBox_2)
        self.clearBtn.setObjectName(u"clearBtn")

        self.gridLayout_2.addWidget(self.clearBtn, 6, 2, 1, 2)

        self.saveBtn = QPushButton(self.groupBox_2)
        self.saveBtn.setObjectName(u"saveBtn")

        self.gridLayout_2.addWidget(self.saveBtn, 6, 0, 1, 2)

        self.recordBtn = QPushButton(self.groupBox_2)
        self.recordBtn.setObjectName(u"recordBtn")

        self.gridLayout_2.addWidget(self.recordBtn, 5, 0, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.textBrowser)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1098, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionRecord)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionClear)
        self.menuEdit.addAction(self.actionAnalysis)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRecord)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAnalysis)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Laser Collimator", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAnalysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionRecord.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Recorded Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Detector Target", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hardware Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resistance:", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.setResistanceBtn.setText(QCoreApplication.translate("MainWindow", u"Set Resistance", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Detector Data", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"D11:", None))
        self.moveEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PRx:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PRy:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D10:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X (\u03bcm):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D00:", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y (\u03bcm):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Move:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"D01:", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.recordBtn.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

