from database.conexao import connect_db  # Importa a função de conexão com o banco de dados
import mysql.connector

class UsuarioModel:
    def fazer_login(self, usuario, senha):
        """
        Valida o login do usuário no banco de dados.
        Retorna o ID do usuário se o login for bem-sucedido, ou None em caso de falha.
        """
        conn = connect_db()  # Usa a função de conexão corretamente
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT id FROM users WHERE username = %s AND password = %s"
                cursor.execute(query, (usuario, senha))
                result = cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    return result[0]  # Retorna o ID do usuário
                else:
                    return None  # Login falhou
            except Exception as e:
                print(f"Erro ao validar login: {e}")
                return None
        else:
            return None  # Falha na conexão com o banco de dados

    def cadastrar_usuario(self, nome, senha, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos):
        try:
            conn = connect_db()  # Aqui deve usar a função importada
            if conn is None:
                return False

            cursor = conn.cursor()

            # Inserir os dados do usuário na tabela users
            query = '''
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            '''
            cursor.execute(query, (nome, senha))

            # Obter o ID do usuário recém-criado
            user_id = cursor.lastrowid

            # Inserir os dados na tabela cadastro
            query = '''
                INSERT INTO cadastro (user_id, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (user_id, salario, despesa, investimentos, rendaextra, veiculos, gasolina, cursos))

            # Commit para salvar as alterações no banco
            conn.commit()
            conn.close()

            return user_id  # Retorna o user_id para o controlador usar (se necessário)
        except mysql.connector.Error as e:
            print(f"Erro ao salvar no banco de dados: {e}")
            conn.rollback()  # Caso ocorra algum erro, faz o rollback para não deixar dados inconsistentes
            return None
