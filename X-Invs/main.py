import sys
from PySide6.QtWidgets import QApplication
from controller.login_controller import LoginController

def main():
    # Cria a aplicação
    app = QApplication(sys.argv)

    # Inicializa o controlador de login
    login_controller = LoginController()

    # Exibe a janela de login
    login_controller.view.show()

    # Executa a aplicação
    sys.exit(app.exec())

if __name__ == "__main__":
    main()