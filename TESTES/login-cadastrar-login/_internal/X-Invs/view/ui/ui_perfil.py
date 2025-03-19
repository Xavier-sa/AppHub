# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfilpoPilK.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Perfil_usuario(object):
    def setupUi(self, Perfil_usuario):
        if not Perfil_usuario.objectName():
            Perfil_usuario.setObjectName(u"Perfil_usuario")
        Perfil_usuario.resize(605, 607)
        Perfil_usuario.setStyleSheet(u"QWidget {\n"
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
        self.label_nome = QLabel(Perfil_usuario)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(50, 20, 150, 16))
        self.label_nome.setStyleSheet(u"color: blue; font: bold 14px;")
        self.label_salario = QLabel(Perfil_usuario)
        self.label_salario.setObjectName(u"label_salario")
        self.label_salario.setGeometry(QRect(50, 60, 150, 16))
        self.label_despesa = QLabel(Perfil_usuario)
        self.label_despesa.setObjectName(u"label_despesa")
        self.label_despesa.setGeometry(QRect(50, 100, 150, 16))
        self.label_investimentos = QLabel(Perfil_usuario)
        self.label_investimentos.setObjectName(u"label_investimentos")
        self.label_investimentos.setGeometry(QRect(50, 140, 150, 16))
        self.label_rendaextra = QLabel(Perfil_usuario)
        self.label_rendaextra.setObjectName(u"label_rendaextra")
        self.label_rendaextra.setGeometry(QRect(50, 180, 150, 16))
        self.label_veiculos = QLabel(Perfil_usuario)
        self.label_veiculos.setObjectName(u"label_veiculos")
        self.label_veiculos.setGeometry(QRect(50, 220, 150, 16))
        self.label_gasolina = QLabel(Perfil_usuario)
        self.label_gasolina.setObjectName(u"label_gasolina")
        self.label_gasolina.setGeometry(QRect(50, 260, 150, 16))
        self.label_cursos = QLabel(Perfil_usuario)
        self.label_cursos.setObjectName(u"label_cursos")
        self.label_cursos.setGeometry(QRect(50, 300, 150, 16))
        self.label_salario_value = QLabel(Perfil_usuario)
        self.label_salario_value.setObjectName(u"label_salario_value")
        self.label_salario_value.setGeometry(QRect(150, 60, 150, 16))
        self.label_despesa_value = QLabel(Perfil_usuario)
        self.label_despesa_value.setObjectName(u"label_despesa_value")
        self.label_despesa_value.setGeometry(QRect(150, 100, 150, 16))
        self.label_investimentos_value = QLabel(Perfil_usuario)
        self.label_investimentos_value.setObjectName(u"label_investimentos_value")
        self.label_investimentos_value.setGeometry(QRect(150, 140, 150, 16))
        self.label_rendaextra_value = QLabel(Perfil_usuario)
        self.label_rendaextra_value.setObjectName(u"label_rendaextra_value")
        self.label_rendaextra_value.setGeometry(QRect(150, 180, 150, 16))
        self.label_veiculos_value = QLabel(Perfil_usuario)
        self.label_veiculos_value.setObjectName(u"label_veiculos_value")
        self.label_veiculos_value.setGeometry(QRect(150, 220, 150, 16))
        self.label_gasolina_value = QLabel(Perfil_usuario)
        self.label_gasolina_value.setObjectName(u"label_gasolina_value")
        self.label_gasolina_value.setGeometry(QRect(150, 260, 150, 16))
        self.label_cursos_value = QLabel(Perfil_usuario)
        self.label_cursos_value.setObjectName(u"label_cursos_value")
        self.label_cursos_value.setGeometry(QRect(150, 300, 150, 16))
        self.btn_fechar = QPushButton(Perfil_usuario)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setGeometry(QRect(250, 550, 100, 40))

        self.retranslateUi(Perfil_usuario)

        QMetaObject.connectSlotsByName(Perfil_usuario)
    # setupUi

    def retranslateUi(self, Perfil_usuario):
        Perfil_usuario.setWindowTitle(QCoreApplication.translate("Perfil_usuario", u"Perfil do Usu\u00e1rio", None))
        self.label_nome.setText(QCoreApplication.translate("Perfil_usuario", u"Bem-vindo, Usu\u00e1rio!", None))
        self.label_salario.setText(QCoreApplication.translate("Perfil_usuario", u"Sal\u00e1rio: ", None))
        self.label_despesa.setText(QCoreApplication.translate("Perfil_usuario", u"Despesa: ", None))
        self.label_investimentos.setText(QCoreApplication.translate("Perfil_usuario", u"Investimentos: ", None))
        self.label_rendaextra.setText(QCoreApplication.translate("Perfil_usuario", u"Renda Extra: ", None))
        self.label_veiculos.setText(QCoreApplication.translate("Perfil_usuario", u"Ve\u00edculos: ", None))
        self.label_gasolina.setText(QCoreApplication.translate("Perfil_usuario", u"Gasolina: ", None))
        self.label_cursos.setText(QCoreApplication.translate("Perfil_usuario", u"Cursos: ", None))
        self.label_salario_value.setText("")
        self.label_despesa_value.setText("")
        self.label_investimentos_value.setText("")
        self.label_rendaextra_value.setText("")
        self.label_veiculos_value.setText("")
        self.label_gasolina_value.setText("")
        self.label_cursos_value.setText("")
        self.btn_fechar.setText(QCoreApplication.translate("Perfil_usuario", u"Fechar", None))
    # retranslateUi

