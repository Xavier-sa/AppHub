from view.cadastro import CadastroView
from model.usuario import UsuarioModel

class CadastroController:
    def __init__(self, user_id):
        self.view = CadastroView()  # Instância da tela de cadastro
        self.model = UsuarioModel()  # Instância do modelo de usuário
        self.user_id = user_id  # Armazena o ID do usuário logado
        self.view.cadastrar_btn.clicked.connect(self.handle_cadastro)
        self.view.voltar_login_btn.clicked.connect(self.voltar_ao_login)

    def handle_cadastro(self):
        # Coletar dados dos campos de entrada
        nome = self.view.nome.text()
        senha = self.view.senha.text()
        salario = self.view.salario.text()
        despesa = self.view.despesa.text()
        investimentos = self.view.investimentos.text()
        rendaextra = self.view.rendaextra.text()
        veiculos = self.view.veiculos.text()
        gasolina = self.view.gasolina.text()
        cursos = self.view.cursos.text()

        # Validar se todos os campos foram preenchidos e são números
        try:
            salario = int(salario)
            despesa = int(despesa)
            investimentos = int(investimentos)
            rendaextra = int(rendaextra)
            veiculos = int(veiculos)
            gasolina = int(gasolina)
            cursos = int(cursos)
        except ValueError:
            print("Todos os campos devem ser números inteiros!")
            return

        # Aqui você pode adicionar a lógica para salvar os dados no banco de dados
        print("Cadastro realizado com sucesso!")
        self.view.close()  # Fecha a janela de cadastro após o sucesso

    def voltar_ao_login(self):
        """Fecha a janela de cadastro e volta para a tela de login."""
        self.view.close()