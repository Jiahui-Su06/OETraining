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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QToolBar,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 622)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSave.setIcon(icon1)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionClose.setIcon(icon2)
        self.actionProcess = QAction(MainWindow)
        self.actionProcess.setObjectName(u"actionProcess")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/process.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionProcess.setIcon(icon3)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon4)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon5)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(640, 480))

        self.verticalLayout.addWidget(self.graphicsView)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.openBtn = QPushButton(self.groupBox_2)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setMaximumSize(QSize(160, 16777215))

        self.gridLayout.addWidget(self.openBtn, 0, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.processBtn = QPushButton(self.groupBox_2)
        self.processBtn.setObjectName(u"processBtn")
        self.processBtn.setMaximumSize(QSize(160, 16777215))

        self.gridLayout.addWidget(self.processBtn, 0, 2, 1, 2)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.zEndEdit = QLineEdit(self.groupBox_2)
        self.zEndEdit.setObjectName(u"zEndEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.zEndEdit.sizePolicy().hasHeightForWidth())
        self.zEndEdit.setSizePolicy(sizePolicy1)
        self.zEndEdit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.zEndEdit, 1, 3, 1, 1)

        self.zStartEdit = QLineEdit(self.groupBox_2)
        self.zStartEdit.setObjectName(u"zStartEdit")
        sizePolicy1.setHeightForWidth(self.zStartEdit.sizePolicy().hasHeightForWidth())
        self.zStartEdit.setSizePolicy(sizePolicy1)
        self.zStartEdit.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.zStartEdit, 1, 1, 1, 1)

        self.proBar = QProgressBar(self.groupBox_2)
        self.proBar.setObjectName(u"proBar")
        sizePolicy1.setHeightForWidth(self.proBar.sizePolicy().hasHeightForWidth())
        self.proBar.setSizePolicy(sizePolicy1)
        self.proBar.setMinimumSize(QSize(0, 0))
        self.proBar.setMaximumSize(QSize(240, 16777215))
        self.proBar.setValue(0)

        self.gridLayout.addWidget(self.proBar, 2, 1, 1, 3)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1015, 33))
        self.menuFile_F = QMenu(self.menubar)
        self.menuFile_F.setObjectName(u"menuFile_F")
        self.menuEdit_E = QMenu(self.menubar)
        self.menuEdit_E.setObjectName(u"menuEdit_E")
        self.menuHelp_H = QMenu(self.menubar)
        self.menuHelp_H.setObjectName(u"menuHelp_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuEdit_E.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menuFile_F.addAction(self.actionOpen)
        self.menuFile_F.addAction(self.actionSave)
        self.menuFile_F.addAction(self.actionClose)
        self.menuFile_F.addSeparator()
        self.menuFile_F.addAction(self.actionQuit)
        self.menuEdit_E.addAction(self.actionProcess)
        self.menuHelp_H.addAction(self.actionHelp)
        self.menuHelp_H.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionProcess)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Digital Holographic Reconstruction System", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionProcess.setText(QCoreApplication.translate("MainWindow", u"Process Image", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End (mm):", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"Process Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start (mm):", None))
        self.zEndEdit.setText(QCoreApplication.translate("MainWindow", u"160", None))
        self.zStartEdit.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Progress:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.menuFile_F.setTitle(QCoreApplication.translate("MainWindow", u"File(&F)", None))
        self.menuEdit_E.setTitle(QCoreApplication.translate("MainWindow", u"Edit(&E)", None))
        self.menuHelp_H.setTitle(QCoreApplication.translate("MainWindow", u"Help(&H)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

