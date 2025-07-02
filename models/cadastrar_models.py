from models.db import conectar

class Cadastrar:
    def __init__(self, nome, email, senha,id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
    
    
    def salvar_cadastrar(self):
        conn = conectar()
        cursor = conn.cursor()
        
        if self._email_existe():
            raise Exception("Email já cadastrado")

        sql = """
        INSERT INTO alunos (nome, email, senha)
        VALUES (%s, %s, %s)
        """
        valores = (self.nome, self.email, self.senha)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    def _email_existe(self):
        conn = conectar()
        cursor = conn.cursor()
        
        sql = "SELECT id_aluno FROM alunos WHERE email = %s"
        cursor.execute(sql, (self.email,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return resultado is not None