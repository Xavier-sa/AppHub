import os

def listar_arquivos(diretorio):
    estrutura = {}
    
    for root, dirs, files in os.walk(diretorio):
        # Obtém o nome do diretório atual sem o caminho completo
        pasta = os.path.relpath(root, diretorio)
        if pasta == ".":
            pasta = ""
        estrutura[pasta] = files
    
    return estrutura

def salvar_estrutura(estrutura, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        for pasta, arquivos in estrutura.items():
            f.write(f"{pasta}/\n")
            for arquivo in arquivos:
                f.write(f"  {arquivo}\n")

# Caminho do seu projeto
diretorio_projeto = r"C:/xampp/htdocs/X-Invs"

# Gera a estrutura do projeto
estrutura = listar_arquivos(diretorio_projeto)

# Salva a estrutura em um arquivo
salvar_estrutura(estrutura, "estrutura_do_projeto.txt")

print("Estrutura do projeto salva com sucesso em 'estrutura_do_projeto.txt'.")
