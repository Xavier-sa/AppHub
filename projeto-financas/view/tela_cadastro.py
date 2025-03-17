# view.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton
from PySide6.QtGui import QIntValidator
from controller import CadastrarUsuario

class CadastroWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Usuário")
        self.setGeometry(100, 100, 400, 500)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        layout = QVBoxLayout()

        # Layout para o formulário
        form_layout = QFormLayout()

        # Campos do formulário
        self.nome = QLineEdit()
        self.senha = QLineEdit()
        self.senha.setEchoMode(QLineEdit.Password)
       
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
        
        # Conectar o botão ao método de cadastro do controller
        self.controller = CadastrarUsuario(self)  # Passando a view para o controller
        self.cadastrar_btn.clicked.connect(self.controller.cadastrar)

        form_layout.addRow(self.cadastrar_btn)

        layout.addLayout(form_layout)
        self.widget.setLayout(layout)
