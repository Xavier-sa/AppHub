# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginMNkrFA.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(412, 400)
        Login.setStyleSheet(u"QWidget {\n"
"    background-color: #222222;\n"
"    color: #FFD700;\n"
"    font-family: 'Arial', sans-serif;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #F57C00;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #333333;\n"
"    color: #FFD700;\n"
"    border: 2px solid #F57C00;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1976D2;\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #F57C00;\n"
"    border-radius: 10px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding: 12px;\n"
"    margin-top: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F57C00;\n"
"    color: #222222;\n"
"    border-color: #FFD700;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D84315;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFD700;\n"
"}")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_logo = QLabel(Login)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_logo)

        self.lineEdit_user = QLineEdit(Login)
        self.lineEdit_user.setObjectName(u"lineEdit_user")

        self.verticalLayout.addWidget(self.lineEdit_user)

        self.lineEdit_password = QLineEdit(Login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.btn_login = QPushButton(Login)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout.addWidget(self.btn_login)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_logo.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:18pt; font-weight:700;\">SENAC HUB </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">XAVIER</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">SOLUTIONS</span></p></body></html>", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Login", u"Digite seu usu\u00e1rio", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Entrar", None))
    # retranslateUi
