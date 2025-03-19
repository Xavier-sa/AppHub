# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrogzhRaL.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CadastroWindow(object):
    def setupUi(self, CadastroWindow):
        if not CadastroWindow.objectName():
            CadastroWindow.setObjectName(u"CadastroWindow")
        CadastroWindow.resize(400, 586)
        CadastroWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(CadastroWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.senha = QLineEdit(self.centralwidget)
        self.senha.setObjectName(u"senha")
        self.senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.senha)

        self.salario = QLineEdit(self.centralwidget)
        self.salario.setObjectName(u"salario")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.salario)

        self.despesa = QLineEdit(self.centralwidget)
        self.despesa.setObjectName(u"despesa")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.despesa)

        self.investimentos = QLineEdit(self.centralwidget)
        self.investimentos.setObjectName(u"investimentos")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.investimentos)

        self.rendaextra = QLineEdit(self.centralwidget)
        self.rendaextra.setObjectName(u"rendaextra")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rendaextra)

        self.veiculos = QLineEdit(self.centralwidget)
        self.veiculos.setObjectName(u"veiculos")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.veiculos)

        self.gasolina = QLineEdit(self.centralwidget)
        self.gasolina.setObjectName(u"gasolina")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.gasolina)

        self.cursos = QLineEdit(self.centralwidget)
        self.cursos.setObjectName(u"cursos")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.cursos)

        self.cadastrar_btn = QPushButton(self.centralwidget)
        self.cadastrar_btn.setObjectName(u"cadastrar_btn")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.cadastrar_btn)

        self.voltar_login_btn = QPushButton(self.centralwidget)
        self.voltar_login_btn.setObjectName(u"voltar_login_btn")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.voltar_login_btn)

        self.nome = QLineEdit(self.centralwidget)
        self.nome.setObjectName(u"nome")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nome)


        self.verticalLayout.addLayout(self.formLayout)

        CadastroWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroWindow)

        QMetaObject.connectSlotsByName(CadastroWindow)
    # setupUi

    def retranslateUi(self, CadastroWindow):
        CadastroWindow.setWindowTitle(QCoreApplication.translate("CadastroWindow", u"Cadastro de Usu\u00e1rio", None))
        self.label_titulo.setText(QCoreApplication.translate("CadastroWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">CADASTRO</span></p></body></html>", None))
        self.senha.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Senha", None))
        self.salario.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Sal\u00e1rio", None))
        self.despesa.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Despesa", None))
        self.investimentos.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Investimentos", None))
        self.rendaextra.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Renda Extra", None))
        self.veiculos.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Ve\u00edculos", None))
        self.gasolina.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Gasolina", None))
        self.cursos.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Cursos", None))
        self.cadastrar_btn.setText(QCoreApplication.translate("CadastroWindow", u"Cadastrar", None))
        self.voltar_login_btn.setText(QCoreApplication.translate("CadastroWindow", u"LOGIN", None))
        self.nome.setPlaceholderText(QCoreApplication.translate("CadastroWindow", u"Nome", None))
    # retranslateUi

