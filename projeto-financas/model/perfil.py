from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton
)
from PySide6.QtGui import QIcon
from .encerrar import Encerrar

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
    text-transform: uppercase;
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




class PerfilWindow(QMainWindow):
    def __init__(self, user_id, username, user_data):
        super().__init__()
        self.user_id = user_id
        self.username = username
        self.user_data = user_data

        self.setWindowTitle("Perfil do Usuário")
        self.setGeometry(100, 100, 400, 500)


        self.setWindowIcon(QIcon("images/icon.png"))  # Altere o caminho para o seu ícone

        # Widget central
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # self.setWindowIcon(QIcon("images/icon.png"))

        # Layout principal
        layout = QVBoxLayout()
        self.setStyleSheet(STYLE)  

        # Exibir o nome do usuário
        self.label_nome = QLabel(f"Bem-vindo, {self.username}!")
        layout.addWidget(self.label_nome)

        # Exibir as informações cadastradas
        self.label_salario = QLabel(f"Salário: {self.user_data['salario']} ")
        self.label_despesa = QLabel(f"Despesa: {self.user_data['despesa']}")
        self.label_investimentos = QLabel(f"Investimentos: {self.user_data['investimentos']}")
        self.label_rendaextra = QLabel(f"Renda Extra: {self.user_data['rendaextra']}")
        self.label_veiculos = QLabel(f"Veículos: {self.user_data['veiculos']}")
        self.label_gasolina = QLabel(f"Gasolina: {self.user_data['gasolina']}")
        self.label_cursos = QLabel(f"Cursos: {self.user_data['cursos']}")

      

        layout.addWidget(self.label_salario)
        layout.addWidget(self.label_despesa)
        layout.addWidget(self.label_investimentos)
        layout.addWidget(self.label_rendaextra)
        layout.addWidget(self.label_veiculos)
        layout.addWidget(self.label_gasolina)
        layout.addWidget(self.label_cursos)

        # Botão para fechar a tela
        self.btn_fechar = QPushButton("Fechar")
        self.btn_fechar.clicked.connect(self.close)
        layout.addWidget(self.btn_fechar)

        # Definir o layout no widget
        self.widget.setLayout(layout)

         # Botão para abrir a tela de "Encerrar"
        self.btn_encerrar = QPushButton("Encerrar")
        self.btn_encerrar.clicked.connect(self.abrir_tela_encerrar)
        layout.addWidget(self.btn_encerrar)

        # Definir o layout no widget
        self.widget.setLayout(layout)

    def abrir_tela_encerrar(self):
        """Abre a tela de encerramento com o GIF"""
        self.encerrar_window = Encerrar()
        self.encerrar_window.show()




