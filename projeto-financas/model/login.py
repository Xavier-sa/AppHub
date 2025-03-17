# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginXqGOyf.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login(QDialog):  # Agora herda de QDialog
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(696, 671)
        Login.setStyleSheet(u"QWidget {\n"
                            "    background-color: #222222;\n"
                            "    color: #FFD700;\n"
                            "    font-family: 'Saiyan Sans', Arial, sans-serif;\n"
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
                            "}\n"
                            "\n"
                            "QMessageBox {\n"
                            "    background-color: #222222;\n"
                            "    color: #FFD700;\n"
                            "    font-size: 16px;\n"
                            "}")

        self.layoutWidget = QWidget(Login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 650, 598))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Logo
        self.alogo = QLabel(self.layoutWidget)
        self.alogo.setObjectName(u"alogo")
        self.alogo.setPixmap(QPixmap(u"../images/teste.PNG"))
        self.gridLayout.addWidget(self.alogo, 0, 0, 1, 1)

        # Caixa de texto para usuário
        self.lineEdit_user = QLineEdit(self.layoutWidget)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.gridLayout.addWidget(self.lineEdit_user, 1, 0, 1, 2)

        # Caixa de texto para senha
        self.lineEdit_password = QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.gridLayout.addWidget(self.lineEdit_password, 2, 0, 1, 2)

        # Botão de login
        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.gridLayout.addWidget(self.btn_login, 3, 0, 1, 2)

        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Login", u"Digite seu usuário", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Entrar", None))

# A função abaixo vai ser utilizada para abrir a tela de login
def abrir_tela_login():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    tela_login = Ui_Login()
    tela_login.exec()

# Inicia o aplicativo e exibe a tela de login
if __name__ == "__main__":
    abrir_tela_login()
