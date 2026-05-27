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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 692)
        icon = QIcon()
        icon.addFile(u":/logo/images/proj7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon()
        icon4.addFile(u":/logo/images/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon4)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon5 = QIcon()
        icon5.addFile(u":/logo/images/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon5)
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
        self.graphicsView.setMinimumSize(QSize(600, 550))

        self.verticalLayout.addWidget(self.graphicsView)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 2)

        self.left_radius_DSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.left_radius_DSpinBox.setObjectName(u"left_radius_DSpinBox")
        self.left_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.left_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout.addWidget(self.left_radius_DSpinBox, 2, 2, 1, 1)

        self.wavelength_DSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.wavelength_DSpinBox.setObjectName(u"wavelength_DSpinBox")
        self.wavelength_DSpinBox.setDecimals(3)
        self.wavelength_DSpinBox.setMaximum(10.000000000000000)
        self.wavelength_DSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.wavelength_DSpinBox, 0, 2, 1, 1)

        self.reset_Button = QPushButton(self.groupBox_2)
        self.reset_Button.setObjectName(u"reset_Button")

        self.gridLayout.addWidget(self.reset_Button, 5, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.cavity_length_DSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.cavity_length_DSpinBox.setObjectName(u"cavity_length_DSpinBox")
        self.cavity_length_DSpinBox.setMaximum(10000.000000000000000)
        self.cavity_length_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout.addWidget(self.cavity_length_DSpinBox, 1, 2, 1, 1)

        self.key_step_DSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.key_step_DSpinBox.setObjectName(u"key_step_DSpinBox")
        self.key_step_DSpinBox.setMaximum(100.000000000000000)
        self.key_step_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout.addWidget(self.key_step_DSpinBox, 4, 2, 1, 1)

        self.right_radius_DSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.right_radius_DSpinBox.setObjectName(u"right_radius_DSpinBox")
        self.right_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.right_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout.addWidget(self.right_radius_DSpinBox, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 2)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 2)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 2)

        self.help_Button = QPushButton(self.groupBox_2)
        self.help_Button.setObjectName(u"help_Button")

        self.gridLayout.addWidget(self.help_Button, 5, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)

        self.distanceEdit = QLineEdit(self.groupBox_4)
        self.distanceEdit.setObjectName(u"distanceEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.distanceEdit.sizePolicy().hasHeightForWidth())
        self.distanceEdit.setSizePolicy(sizePolicy1)
        self.distanceEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.distanceEdit, 8, 1, 1, 1)

        self.d1Box = QDoubleSpinBox(self.groupBox_4)
        self.d1Box.setObjectName(u"d1Box")
        self.d1Box.setMaximum(500.000000000000000)
        self.d1Box.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.d1Box, 5, 1, 1, 1)

        self.wasitEdit = QLineEdit(self.groupBox_4)
        self.wasitEdit.setObjectName(u"wasitEdit")
        sizePolicy1.setHeightForWidth(self.wasitEdit.sizePolicy().hasHeightForWidth())
        self.wasitEdit.setSizePolicy(sizePolicy1)
        self.wasitEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.wasitEdit, 7, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.fBox = QDoubleSpinBox(self.groupBox_4)
        self.fBox.setObjectName(u"fBox")
        self.fBox.setMaximum(200.000000000000000)
        self.fBox.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.fBox, 3, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 2, 2)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.d2Box = QDoubleSpinBox(self.groupBox_4)
        self.d2Box.setObjectName(u"d2Box")
        self.d2Box.setMaximum(700.000000000000000)
        self.d2Box.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.d2Box, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 945, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp_H = QMenu(self.menubar)
        self.menuHelp_H.setObjectName(u"menuHelp_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp_H.addAction(self.actionHelp)
        self.menuHelp_H.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Laser Resonator Designer", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Viewer", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Resonator Parameters", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Right Mirror Radius (mm):", None))
        self.reset_Button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Wavelength (\u03bcm):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Left Mirror Radius (mm):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cavity Length (mm):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Function Key Step (mm):", None))
        self.help_Button.setText(QCoreApplication.translate("MainWindow", u"Function Key Help", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Collimator", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"View Length (mm):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gap Length (mm):", None))
        self.distanceEdit.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.wasitEdit.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Focal Length (mm):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Waist From Lens (mm):", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Fitted with a collimating lens", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Waist Width (mm):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lens Part Number:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File(&F)", None))
        self.menuHelp_H.setTitle(QCoreApplication.translate("MainWindow", u"Help(&H)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

