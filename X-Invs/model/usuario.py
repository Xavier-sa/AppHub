from database.conexao import connect_db  # Importa a função de conexão com o banco de dados

class UsuarioModel:
    def fazer_login(self, usuario, senha):
        """
        Valida o login do usuário no banco de dados.
        Retorna o ID do usuário se o login for bem-sucedido, ou None em caso de falha.
        """
        conn = connect_db()
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

    def cadastrar_usuario(self, username, password):
        """
        Cadastra um novo usuário no banco de dados.
        Retorna True se o cadastro for bem-sucedido, ou False em caso de falha.
        """
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                conn.commit()
                cursor.close()
                conn.close()
                return True  # Cadastro bem-sucedido
            except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}")
                return False
        else:
            return False  # Falha na conexão com o banco de dados