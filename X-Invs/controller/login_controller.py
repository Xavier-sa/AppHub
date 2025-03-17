from view.login import LoginView
from model.usuario import UsuarioModel
from controller.cadastro_controller import CadastroController  # Importe o CadastroController

class LoginController:
    def __init__(self):
        self.view = LoginView()  # Instância da tela de login
        self.model = UsuarioModel()  # Instância do modelo de usuário
        self.view.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        usuario = self.view.lineEdit_user.text()
        senha = self.view.lineEdit_password.text()
        user_id = self.model.fazer_login(usuario, senha)

        if user_id:
            print("Login bem-sucedido!")
            self.view.close()  # Fecha a janela de login

            # Abre a janela de cadastro com o user_id
            self.cadastro_controller = CadastroController(user_id)  # Cria uma instância do CadastroController
            self.cadastro_controller.view.show()  # Exibe a tela de cadastro
        else:
            print("Usuário ou senha incorretos!")