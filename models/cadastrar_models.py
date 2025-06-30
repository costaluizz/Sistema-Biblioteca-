from db import conectar

class Cadastrar:
    def __init__(self,nome,email,senha,tipo,id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
    
    def salvar_cadastrar(self):
        conn = conectar()
        cursor = conn.cursor()
        
       
        sql = """
        INSERT INTO alunos (nome, email, senha)
        VALUES (%s, %s, %s)
        """
        valores = (self.nome, self.email, self.senha)

      

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()











             