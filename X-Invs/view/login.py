from PySide6.QtWidgets import QDialog
from view.ui.ui_login import Ui_Login  # Importe a classe correta

class LoginView(QDialog, Ui_Login):  # Herda de QDialog e Ui_Login
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle("Login")  # Define o título da janela
        self.resize(412, 400)  # Define o tamanho da janela