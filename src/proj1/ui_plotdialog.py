# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 600)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.xVarEdit = QLineEdit(self.groupBox)
        self.xVarEdit.setObjectName(u"xVarEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xVarEdit.sizePolicy().hasHeightForWidth())
        self.xVarEdit.setSizePolicy(sizePolicy)
        self.xVarEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.xVarEdit, 1, 3, 1, 1)

        self.xWidget = QWidget(self.groupBox)
        self.xWidget.setObjectName(u"xWidget")

        self.gridLayout.addWidget(self.xWidget, 0, 0, 1, 4)

        self.xEqEdit = QLineEdit(self.groupBox)
        self.xEqEdit.setObjectName(u"xEqEdit")
        self.xEqEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.xEqEdit, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.yVarEdit = QLineEdit(self.groupBox_2)
        self.yVarEdit.setObjectName(u"yVarEdit")
        sizePolicy.setHeightForWidth(self.yVarEdit.sizePolicy().hasHeightForWidth())
        self.yVarEdit.setSizePolicy(sizePolicy)
        self.yVarEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.yVarEdit, 1, 3, 1, 1)

        self.yWidget = QWidget(self.groupBox_2)
        self.yWidget.setObjectName(u"yWidget")

        self.gridLayout_2.addWidget(self.yWidget, 0, 0, 1, 4)

        self.yEqEdit = QLineEdit(self.groupBox_2)
        self.yEqEdit.setObjectName(u"yEqEdit")
        self.yEqEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.yEqEdit, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Analysis Plotter", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"X-direction Displacement", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Variance:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Fitted Line Equation:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Y-direction Displacement", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Variance:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Fitted Line Equation:", None))
    # retranslateUi

