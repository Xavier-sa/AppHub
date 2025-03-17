# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statusamgKlZ.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_atribuir_pontos(object):
    def setupUi(self, atribuir_pontos):
        if not atribuir_pontos.objectName():
            atribuir_pontos.setObjectName(u"atribuir_pontos")
        atribuir_pontos.resize(578, 667)
        self.label = QLabel(atribuir_pontos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 300, 341, 61))
        self.label_2 = QLabel(atribuir_pontos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 360, 49, 16))
        self.lineEdit = QLineEdit(atribuir_pontos)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 360, 113, 22))
        self.label_3 = QLabel(atribuir_pontos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 400, 49, 16))
        self.label_4 = QLabel(atribuir_pontos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 440, 49, 16))
        self.lineEdit_ki = QLineEdit(atribuir_pontos)
        self.lineEdit_ki.setObjectName(u"lineEdit_ki")
        self.lineEdit_ki.setGeometry(QRect(110, 400, 113, 22))
        self.lineEdit_forca = QLineEdit(atribuir_pontos)
        self.lineEdit_forca.setObjectName(u"lineEdit_forca")
        self.lineEdit_forca.setGeometry(QRect(110, 440, 113, 22))
        self.label_5 = QLabel(atribuir_pontos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 501, 291))
        self.label_5.setPixmap(QPixmap(u"./images/x.JPG"))
        self.pushButton = QPushButton(atribuir_pontos)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 620, 75, 24))
        self.lineEdit_ki.raise_()
        self.lineEdit_forca.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()

        self.retranslateUi(atribuir_pontos)

        QMetaObject.connectSlotsByName(atribuir_pontos)
    # setupUi

    def retranslateUi(self, atribuir_pontos):
        atribuir_pontos.setWindowTitle(QCoreApplication.translate("atribuir_pontos", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("atribuir_pontos", u"Adicione Pontos!", None))
        self.label_2.setText(QCoreApplication.translate("atribuir_pontos", u"Life", None))
        self.label_3.setText(QCoreApplication.translate("atribuir_pontos", u"KI", None))
        self.label_4.setText(QCoreApplication.translate("atribuir_pontos", u"Forca", None))
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("atribuir_pontos", u"Enviar", None))
    # retranslateUi

