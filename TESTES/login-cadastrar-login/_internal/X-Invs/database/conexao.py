import mysql.connector
from PySide6.QtWidgets import QMessageBox

def connect_db():
    """Conecta ao banco de dados"""
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="",
            database="mau_mau"
        )
        if conn.is_connected():
            print("Conexão com o banco de dados estabelecida.")
            return conn
    except mysql.connector.Error as err:
        # Exibe a mensagem de erro em um QMessageBox
        QMessageBox.critical(None, "Erro de Conexão", f"Erro ao conectar ao banco de dados: {err}")
        return None
    

# connect_db() ok funcionou