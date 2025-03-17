# Dicionário para armazenar os usuários
usuarios = {
    "xavier": {"senha": "1234", "renda": 5000, "despesa": 3000}
}

def login(usuario, senha):
    """Função para verificar login."""
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return True
    return False

def cadastrar_usuario(nome, senha, renda, despesa, investimentos, renda_extra, veiculo, gasolina, cursos):
    """Função para cadastrar um novo usuário."""
    if nome not in usuarios:
        usuarios[nome] = {
            "senha": senha,
            "renda": renda,
            "despesa": despesa,
            "investimentos": investimentos,
            "renda_extra": renda_extra,
            "veiculo": veiculo,
            "gasolina": gasolina,
            "cursos": cursos
        }
        return True
    return False

def tela_login():
    """Simula a tela de login."""
    while True:
        print(f"\n{'-'*10}Tela Login{'-'*10}")
        print("1. Fazer login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario_input = input("Digite o nome de usuário: ")
            senha_input = input("Digite a senha: ")

            if login(usuario_input, senha_input):
                print(f"\nLogin bem-sucedido! Bem-vindo, {usuario_input}.")
                perfil(usuario_input)  # Chama a função de perfil após o login
            else:
                print("\nUsuário ou senha incorretos!")
        elif opcao == "2":
            tela_cadastro()  # Chama a tela de cadastro
        elif opcao == "3":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

def tela_cadastro():
    """Simula a tela de cadastro de novos usuários."""
    print("\nCadastro de Novo Usuário")
    novo_usuario = input("Digite o nome do novo usuário: ")
    nova_senha = input("Digite a senha para o novo usuário: ")

   
    try:
        nova_renda = float(input("Digite a renda do novo usuário: "))
        nova_despesa = float(input("Digite a despesa do novo usuário: "))
        investimentos = float(input("Digite o valor dos investimentos: "))
        renda_extra = float(input("Digite a renda extra: "))
        veiculo = input("Digite o tipo de veículo: ")
        gasolina = float(input("Digite o valor gasto com gasolina: "))
        cursos = input("Digite os cursos que o usuário faz: ")

        if cadastrar_usuario(novo_usuario, nova_senha, nova_renda, nova_despesa, investimentos, renda_extra, veiculo, gasolina, cursos):
            print(f"\nUsuário {novo_usuario} cadastrado com sucesso!")
            voltar_ao_login(novo_usuario)  
        else:
            print("\nErro: Usuário já cadastrado.")
    
    except ValueError:
        print("\nErro: A renda, despesa, investimentos e outros valores devem ser números válidos.")

def perfil(usuario):
    """Exibe o perfil do usuário."""
    usuario_info = usuarios[usuario]
    print(f"\nPerfil de {usuario}:")
    print(f"Renda: R$ {usuario_info['renda']}")
    print(f"Despesa: R$ {usuario_info['despesa']}")
    print(f"Investimentos: R$ {usuario_info['investimentos']}")
    print(f"Renda Extra: R$ {usuario_info['renda_extra']}")
    print(f"Veículo: {usuario_info['veiculo']}")
    print(f"Gasolina: R$ {usuario_info['gasolina']}")
    print(f"Cursos: {usuario_info['cursos']}")

    fechar_input = input("\nDigite 'fechar' para sair para a tela de login: ")
    if fechar_input.lower() == 'fechar':
        print("\nVoltando à tela de login...")
        tela_login() 

def voltar_ao_login(usuario_cadastrado):
    """Volta ao login e informa o login cadastrado."""
    print("\nVoltando à tela de login...")
    print(f"Usuário {usuario_cadastrado} foi cadastrado com sucesso!")
    tela_login() 


def main():
    tela_login()

if __name__ == "__main__":
    main()