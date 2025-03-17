import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
import mysql.connector
from model.login import Ui_Login  
from model.cadastrar import CadastroWindow
from model.perfil import PerfilWindow
# Estilo CSS
# Estilo CSS (sem a propriedade transition)
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





class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.user_id = None

        self.setStyleSheet(STYLE)  


        self.ui.btn_login.clicked.connect(self.check_login)

    def connect_db(self):
        """Conecta ao banco de dados"""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="mau_mau"
            )
            return conn
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Erro", f"Erro ao conectar ao banco de dados: {err}")
            return None

    def check_login(self):
        """Verifica o login do usuário"""
        usuario = self.ui.lineEdit_user.text()
        senha = self.ui.lineEdit_password.text()

        conn = self.connect_db()
        if conn is None:
            return

        cursor = conn.cursor()
        query = "SELECT id, username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (usuario, senha))
        user = cursor.fetchone()

        if user:
            self.user_id, self.username = user  # Armazena ID e Nome
            QMessageBox.information(self, "Login", "Login bem-sucedido!")
            self.close()
           
            # Abrir a janela de cadastro após o login
            self.cadastro_window = CadastroWindow()
            self.cadastro_window.show()
            
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!")

        cursor.close()
        conn.close()
        

    

# Inicializa o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())