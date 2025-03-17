import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

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