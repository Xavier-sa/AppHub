from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QMessageBox
from view.cadastro import CadastroView
from model.usuario import UsuarioModel

class CadastroController(QObject):
    voltar_login_signal = Signal()  # Sinal para notificar o retorno ao login

    def __init__(self, user_id):
        super().__init__()
        self.view = CadastroView()  # Instância da tela de cadastro
        self.model = UsuarioModel()  # Instância do modelo de usuário
        self.user_id = user_id  # Armazena o ID do usuário logado
        self.view.cadastrar_btn.clicked.connect(self.handle_cadastro)
        self.view.voltar_login_btn.clicked.connect(self.voltar_ao_login)

    def handle_cadastro(self):
        # Coletar dados dos campos de entrada
        nome = self.view.nome.text().strip()
        senha = self.view.senha.text().strip()
        salario = self.view.salario.text().strip()
        despesa = self.view.despesa.text().strip()
        investimentos = self.view.investimentos.text().strip()
        rendaextra = self.view.rendaextra.text().strip()
        veiculos = self.view.veiculos.text().strip()
        gasolina = self.view.gasolina.text().strip()
        cursos = self.view.cursos.text().strip()

        # Validar se todos os campos foram preenchidos
        if not all([nome, senha, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos]):
            self.show_message("Todos os campos devem ser preenchidos!", "Erro", QMessageBox.Critical)
            return

        # Validar se os campos numéricos são números inteiros
        try:
            salario = int(salario)
            despesa = int(despesa)
            investimentos = int(investimentos)
            rendaextra = int(rendaextra)
            veiculos = int(veiculos)
            gasolina = int(gasolina)
            cursos = int(cursos)
        except ValueError:
            self.show_message("Todos os campos numéricos devem ser números inteiros!", "Erro", QMessageBox.Critical)
            return

        # Salvar os dados no banco de dados usando o UsuarioModel
        user_id = self.model.cadastrar_usuario(nome, senha, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos)

        if user_id:
            self.show_message("Cadastro realizado com sucesso!", "Sucesso", QMessageBox.Information)
            self.clear_fields()
        else:
            self.show_message("Erro ao salvar os dados no banco de dados.", "Erro", QMessageBox.Critical)

    def voltar_ao_login(self):
        """Fecha a janela de cadastro e emite o sinal para voltar ao login."""
        self.view.close()
        self.voltar_login_signal.emit()  # Emite o sinal

    def show_message(self, message, title, icon_type):
        """Exibe uma caixa de mensagem com o conteúdo e estilo personalizado."""
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

    def clear_fields(self):
        """Limpa os campos do formulário."""
        self.view.nome.clear()
        self.view.senha.clear()
        self.view.salario.clear()
        self.view.despesa.clear()
        self.view.investimentos.clear()
        self.view.rendaextra.clear()
        self.view.veiculos.clear()
        self.view.gasolina.clear()
        self.view.cursos.clear()