# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGraphicsView, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(918, 701)
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 10, 622, 633))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(630, 20, 272, 621))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.left_radius_DSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.left_radius_DSpinBox.setObjectName(u"left_radius_DSpinBox")
        self.left_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.left_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.left_radius_DSpinBox, 3, 1, 1, 1)

        self.wavelength_DSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.wavelength_DSpinBox.setObjectName(u"wavelength_DSpinBox")
        self.wavelength_DSpinBox.setDecimals(3)
        self.wavelength_DSpinBox.setMaximum(10.000000000000000)
        self.wavelength_DSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout_2.addWidget(self.wavelength_DSpinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 9, 0, 1, 2)

        self.right_radius_DSpinBox_2 = QDoubleSpinBox(self.layoutWidget)
        self.right_radius_DSpinBox_2.setObjectName(u"right_radius_DSpinBox_2")
        self.right_radius_DSpinBox_2.setMaximum(10000.000000000000000)
        self.right_radius_DSpinBox_2.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.right_radius_DSpinBox_2, 5, 1, 1, 1)

        self.cavity_length_DSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.cavity_length_DSpinBox.setObjectName(u"cavity_length_DSpinBox")
        self.cavity_length_DSpinBox.setMaximum(10000.000000000000000)
        self.cavity_length_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.cavity_length_DSpinBox, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.reset_Button = QPushButton(self.layoutWidget)
        self.reset_Button.setObjectName(u"reset_Button")

        self.gridLayout_2.addWidget(self.reset_Button, 8, 1, 1, 1)

        self.help_Button = QPushButton(self.layoutWidget)
        self.help_Button.setObjectName(u"help_Button")

        self.gridLayout_2.addWidget(self.help_Button, 8, 0, 1, 1)

        self.key_step_DSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.key_step_DSpinBox.setObjectName(u"key_step_DSpinBox")
        self.key_step_DSpinBox.setMaximum(100.000000000000000)
        self.key_step_DSpinBox.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.key_step_DSpinBox, 7, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.right_radius_DSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.right_radius_DSpinBox.setObjectName(u"right_radius_DSpinBox")
        self.right_radius_DSpinBox.setMaximum(10000.000000000000000)
        self.right_radius_DSpinBox.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.right_radius_DSpinBox, 4, 1, 1, 1)

        self.cavity_length_DSpinBox_2 = QDoubleSpinBox(self.layoutWidget)
        self.cavity_length_DSpinBox_2.setObjectName(u"cavity_length_DSpinBox_2")
        self.cavity_length_DSpinBox_2.setMaximum(10000.000000000000000)
        self.cavity_length_DSpinBox_2.setSingleStep(10.000000000000000)

        self.gridLayout_2.addWidget(self.cavity_length_DSpinBox_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.right_radius_DSpinBox_3 = QDoubleSpinBox(self.layoutWidget)
        self.right_radius_DSpinBox_3.setObjectName(u"right_radius_DSpinBox_3")
        self.right_radius_DSpinBox_3.setMaximum(10000.000000000000000)
        self.right_radius_DSpinBox_3.setSingleStep(50.000000000000000)

        self.gridLayout_2.addWidget(self.right_radius_DSpinBox_3, 6, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Cavity Length (mm)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Mirror Radius (mm)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Function Key Step (mm)", None))
        self.reset_Button.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.help_Button.setText(QCoreApplication.translate("Form", u"Function Key Help", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Wavelength (\u03bcm)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Fold Angle (\u00b0)", None))
    # retranslateUi

