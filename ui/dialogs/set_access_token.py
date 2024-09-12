# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_access_token.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_dialog_setAccessToken(object):
    def setupUi(self, dialog_setAccessToken):
        if not dialog_setAccessToken.objectName():
            dialog_setAccessToken.setObjectName(u"dialog_setAccessToken")
        dialog_setAccessToken.resize(536, 72)
        self.gridLayout = QGridLayout(dialog_setAccessToken)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_accessToken = QLabel(dialog_setAccessToken)
        self.label_accessToken.setObjectName(u"label_accessToken")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_accessToken)

        self.lineEdit_accessToken = QLineEdit(dialog_setAccessToken)
        self.lineEdit_accessToken.setObjectName(u"lineEdit_accessToken")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_accessToken)

        self.buttonBox = QDialogButtonBox(dialog_setAccessToken)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.buttonBox)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(dialog_setAccessToken)

        QMetaObject.connectSlotsByName(dialog_setAccessToken)
    # setupUi

    def retranslateUi(self, dialog_setAccessToken):
        dialog_setAccessToken.setWindowTitle(QCoreApplication.translate("dialog_setAccessToken", u"Set Access Token", None))
        self.label_accessToken.setText(QCoreApplication.translate("dialog_setAccessToken", u"Access Token:", None))
        self.lineEdit_accessToken.setText("")
        self.lineEdit_accessToken.setPlaceholderText(QCoreApplication.translate("dialog_setAccessToken", u"New Token", None))
    # retranslateUi

