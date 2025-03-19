# from PySide6.QtCore import Signal, QObject
# from view.login import LoginView
# from model.usuario import UsuarioModel

# class LoginController(QObject):  # Herda de QObject para usar sinais
#     login_sucesso = Signal(int)  # Sinal para notificar o login bem-sucedido

#     def __init__(self):
#         super().__init__()
#         self.view = LoginView()  # Instância da tela de login
#         self.model = UsuarioModel()  # Instância do modelo de usuário
#         self.view.btn_login.clicked.connect(self.handle_login)

#     def handle_login(self):
#         usuario = self.view.lineEdit_user.text()
#         senha = self.view.lineEdit_password.text()
#         user_id = self.model.fazer_login(usuario, senha)

#         if user_id:
#             print("Login bem-sucedido!")
#             self.login_sucesso.emit(user_id)  # Emite o sinal com o user_id
#         else:
#             print("Usuário ou senha incorretos!")




from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QMessageBox  # Importando a classe QMessageBox
from view.login import LoginView
from model.usuario import UsuarioModel

class LoginController(QObject):  # Herda de QObject para usar sinais
    login_sucesso = Signal(int)  # Sinal para notificar o login bem-sucedido

    def __init__(self):
        super().__init__()
        self.view = LoginView()  # Instância da tela de login
        self.model = UsuarioModel()  # Instância do modelo de usuário
        self.view.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        usuario = self.view.lineEdit_user.text()
        senha = self.view.lineEdit_password.text()
        user_id = self.model.fazer_login(usuario, senha)

        if user_id:
            self.show_message("Login bem-sucedido!", "Sucesso", QMessageBox.Information)
            self.login_sucesso.emit(user_id)  # Emite o sinal com o user_id
        else:
            self.show_message("Usuário ou senha incorretos!", "Erro", QMessageBox.Critical)

    def show_message(self, message, title, icon_type):
        # Exibe uma caixa de mensagem com o conteúdo
        msg = QMessageBox()
        msg.setIcon(icon_type)  # Define o ícone (informação ou erro)
        msg.setText(message)  # Define o texto da mensagem
        msg.setWindowTitle(title)  # Define o título da caixa
       



         # Aplica o estilo personalizado
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #f2f2f2;
                font-size: 14px;
                color: #333;
                border-radius: 10px;
            }
            QLabel {
                color: #007bff;
                font-weight: bold;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        msg.exec()  # Exibe a caixa de mensagem
