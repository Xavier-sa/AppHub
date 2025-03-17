import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget



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

class Encerrar(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout()

        # Cria o QLabel onde o GIF será exibido
        label = QLabel(self)
        
        # Carrega o GIF usando QMovie
        movie = QMovie("images/goku.gif")
        
        # Define o movie no QLabel
        label.setMovie(movie)
        
        # Inicia a animação do GIF
        movie.start()

        # Adiciona o QLabel ao layout
        layout.addWidget(label)

        # Configura o layout na janela principal
        self.setLayout(layout)
        self.setWindowTitle("Exemplo de GIF com PySide6")
        self.setGeometry(100, 100, 400, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Encerrar()
    window.show()
    sys.exit(app.exec())