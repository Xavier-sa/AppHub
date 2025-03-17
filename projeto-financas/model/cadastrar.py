# -*- coding: utf-8 -*-

import sys
import mysql.connector
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator,QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QFormLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox
)

from .perfil import PerfilWindow

STYLE = """
QWidget {
    background-color: #222222;
    color: #FFD700;
    font-family: 'Saiyan Sans', Arial, sans-serif;
}

QLabel {
    color: #F57C00;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
}

QLineEdit {
    background-color: #333333;
    color: #FFD700;
    border: 2px solid #F57C00;
    border-radius: 8px;
    padding: 10px;
    font-size: 18px;
}

QPushButton {
    background-color: #1976D2;
    color: #FFFFFF;
    border: 2px solid #F57C00;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
    padding: 12px;
    margin-top: 15px;
}

QPushButton:hover {
    background-color: #F57C00;
    color: #222222;
    border-color: #FFD700;
}

QPushButton:pressed {
    background-color: #D84315;
}

QLineEdit:focus {
    border: 2px solid #FFD700;
}

QMessageBox {
    background-color: #222222;
    color: #FFD700;
    font-size: 16px;
}
"""




class CadastroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Usuário")
        self.setGeometry(100, 100, 400, 300)

        self.setWindowIcon(QIcon("images/icon.png")) 
       

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        layout = QVBoxLayout()

        # Layout para o formulário
        form_layout = QFormLayout()

        # Campos do formulário
        self.nome = QLineEdit()
        self.senha = QLineEdit()
        self.senha.setEchoMode(QLineEdit.Password)
        


        self.setStyleSheet(STYLE)  

        self.salario = QLineEdit()
        self.salario.setValidator(QIntValidator())  # Validador para números inteiros
        self.despesa = QLineEdit()
        self.despesa.setValidator(QIntValidator())  # Validador para números inteiros
        self.investimentos = QLineEdit()
        self.investimentos.setValidator(QIntValidator())  # Validador para números inteiros
        self.rendaextra = QLineEdit()
        self.veiculos = QLineEdit()
        self.gasolina = QLineEdit()
        self.cursos = QLineEdit()

        # Adicionar os campos ao layout do formulário
        form_layout.addRow("Nome", self.nome)
        form_layout.addRow("Senha", self.senha)
        form_layout.addRow("Salário", self.salario)
        form_layout.addRow("Despesa", self.despesa)
        form_layout.addRow("Investimentos", self.investimentos)
        form_layout.addRow("Renda Extra", self.rendaextra)
        form_layout.addRow("Veículos", self.veiculos)
        form_layout.addRow("Gasolina", self.gasolina)
        form_layout.addRow("Cursos", self.cursos)

        # Botão de cadastro
        self.cadastrar_btn = QPushButton("Cadastrar")
        self.cadastrar_btn.clicked.connect(self.cadastrar)  # Conectando o botão à função
        form_layout.addRow(self.cadastrar_btn)

        layout.addLayout(form_layout)
        self.widget.setLayout(layout)

   
        
    def connect_db(self):
        """Conecta ao banco de dados MySQL usando o endereço 127.0.0.1 e a porta 3306"""
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",  
                port=3306,  
                user="root",  
                password="", 
                database="mau_mau"  
            )
            return conn
        except mysql.connector.Error as err:
            self.show_message("Erro", f"Erro ao conectar ao banco de dados: {err}")
            return None


    def cadastrar(self):
        # Validação dos dados
        if not self.nome.text():
            self.show_message("Erro", "O campo 'Nome' é obrigatório.")
            return
       
        if not self.salario.text() or not self.despesa.text():  # Verificar se os campos não estão vazios
            self.show_message("Erro", "Salário e Despesa são obrigatórios.")
            return
        
        # Inserir dados no banco de dados
        self.salvar_no_banco()

    def salvar_no_banco(self):
        try:
            # Conectar ao banco de dados
            conn = self.connect_db()
            if conn is None:
                return

            cursor = conn.cursor()

            # Inserir os dados na tabela users
            cursor.execute('''
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            ''', (self.nome.text(), self.senha.text()))

            # Obter o ID do usuário recém-criado
            user_id = cursor.lastrowid

            # Inserir os dados na tabela cadastro
            cursor.execute('''
                INSERT INTO cadastro (user_id, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (user_id, self.salario.text(), self.despesa.text(), 
                  self.investimentos.text(), self.rendaextra.text(),
                  self.veiculos.text(), self.gasolina.text(), self.cursos.text()))

            # Salvar as alterações e fechar a conexão
            conn.commit()
            conn.close()

            # Dados do usuário para exibir no perfil
            user_data = {
                "salario": self.salario.text(),
                "despesa": self.despesa.text(),
                "investimentos": self.investimentos.text(),
                "rendaextra": self.rendaextra.text(),
                "veiculos": self.veiculos.text(),
                "gasolina": self.gasolina.text(),
                "cursos": self.cursos.text()
            }

            # Fechar a janela de cadastro
            self.close()

            # Abrir a tela de perfil
            self.perfil_window = PerfilWindow(user_id, self.nome.text(), user_data)
            self.perfil_window.show()

            self.show_message("Sucesso", "Cadastro realizado com sucesso!")
        except mysql.connector.Error as e:
            self.show_message("Erro", f"Erro ao salvar no banco de dados: {e}")

    def show_message(self, title, message):
        # Função para exibir uma mensagem
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information if title == "Sucesso" else QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()