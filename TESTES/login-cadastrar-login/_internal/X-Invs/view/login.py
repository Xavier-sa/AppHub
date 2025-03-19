from PySide6.QtWidgets import QDialog
from view.ui.ui_login import Ui_Login  # Importe a classe correta
from PySide6.QtGui import QIcon

class LoginView(QDialog, Ui_Login):  # Herda de QDialog e Ui_Login
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle("Login")  # Define o título da janela
        self.resize(412, 400)  # Define o tamanho da janela
        self.setWindowIcon(QIcon("C:/xampp/htdocs/X-Invs/view/images/icon.png"))  # Caminho para o ícone