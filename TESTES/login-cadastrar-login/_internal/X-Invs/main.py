import sys
from PySide6.QtWidgets import QApplication
from controller.login_controller import LoginController
from controller.cadastro_controller import CadastroController

def main():
   
    app = QApplication(sys.argv)

    
    def abrir_login():
        login_controller = LoginController()
        login_controller.view.show()

        
        def abrir_cadastro(user_id):
            login_controller.view.close()  
            abrir_cadastro_tela(user_id)  

        login_controller.login_sucesso.connect(abrir_cadastro)

        return login_controller

    
    def abrir_cadastro_tela(user_id):
        cadastro_controller = CadastroController(user_id)
        cadastro_controller.view.show()

        # Conecta o sinal de voltar ao login
        def voltar_ao_login():
            cadastro_controller.view.close()  
            abrir_login()  

        cadastro_controller.voltar_login_signal.connect(voltar_ao_login)

    
    abrir_login()

    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()