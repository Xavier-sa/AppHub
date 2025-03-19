from PySide6.QtWidgets import QMainWindow
from view.ui.ui_cadastro import Ui_CadastroWindow  # Importe a classe correta
from PySide6.QtGui import QIcon

class CadastroView(QMainWindow, Ui_CadastroWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle("Cadastro")  # Define o título da janela
        self.resize(400, 586)  # Define o tamanho da janela
        self.setWindowIcon(QIcon("C:/xampp/htdocs/X-Invs/view/images/icon.png"))  # Caminho para o ícone