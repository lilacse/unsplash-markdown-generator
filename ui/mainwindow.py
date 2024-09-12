# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(887, 573)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(6)
        self.label_accessToken = QLabel(self.centralwidget)
        self.label_accessToken.setObjectName(u"label_accessToken")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_accessToken)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_accessTokenValue = QLabel(self.centralwidget)
        self.label_accessTokenValue.setObjectName(u"label_accessTokenValue")

        self.horizontalLayout.addWidget(self.label_accessTokenValue)

        self.pushButton_setAccessToken = QPushButton(self.centralwidget)
        self.pushButton_setAccessToken.setObjectName(u"pushButton_setAccessToken")

        self.horizontalLayout.addWidget(self.pushButton_setAccessToken)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.lable_url = QLabel(self.centralwidget)
        self.lable_url.setObjectName(u"lable_url")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lable_url)

        self.lineEdit_url = QLineEdit(self.centralwidget)
        self.lineEdit_url.setObjectName(u"lineEdit_url")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_url)

        self.pushButton_generate = QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName(u"pushButton_generate")

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.pushButton_generate)

        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_result)

        self.dummy_result = QLabel(self.centralwidget)
        self.dummy_result.setObjectName(u"dummy_result")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dummy_result)

        self.plainTextEdit_result = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_result.setObjectName(u"plainTextEdit_result")
        self.plainTextEdit_result.setReadOnly(False)

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.plainTextEdit_result)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unsplash Markdown Generator", None))
        self.label_accessToken.setText(QCoreApplication.translate("MainWindow", u"Access Token:", None))
        self.label_accessTokenValue.setText(QCoreApplication.translate("MainWindow", u"Not set", None))
        self.pushButton_setAccessToken.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.lable_url.setText(QCoreApplication.translate("MainWindow", u"Unsplash URL:", None))
        self.lineEdit_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://unsplash.com/photos/...", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.dummy_result.setText("")
    # retranslateUi

