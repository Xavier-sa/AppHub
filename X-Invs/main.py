import sys
from PySide6.QtWidgets import QApplication
from controller.login_controller import LoginController
from controller.cadastro_controller import CadastroController

def main():
    # Cria a aplicação
    app = QApplication(sys.argv)

    # Função para abrir a tela de login
    def abrir_login():
        login_controller = LoginController()
        login_controller.view.show()

        # Conecta o sinal de login bem-sucedido para abrir o cadastro
        def abrir_cadastro(user_id):
            login_controller.view.close()  # Fecha a tela de login
            abrir_cadastro_tela(user_id)  # Abre a tela de cadastro

        login_controller.login_sucesso.connect(abrir_cadastro)

        return login_controller

    # Função para abrir a tela de cadastro
    def abrir_cadastro_tela(user_id):
        cadastro_controller = CadastroController(user_id)
        cadastro_controller.view.show()

        # Conecta o sinal de voltar ao login
        def voltar_ao_login():
            cadastro_controller.view.close()  # Fecha a tela de cadastro
            abrir_login()  # Reabre a tela de login

        cadastro_controller.voltar_login_signal.connect(voltar_ao_login)

    # Inicia o ciclo com a tela de login
    abrir_login()

    # Executa a aplicação
    sys.exit(app.exec())

if __name__ == "__main__":
    main()