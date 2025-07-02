from models.db import conectar

class Login:
    def __init__(self, email, senha, tipo):
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.id = None

    def consultar_login(self):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        resultado = None

        if self.tipo == 'aluno':
            sql = "SELECT * FROM alunos WHERE email = %s AND senha = %s"
        elif self.tipo == 'funcionario':
            sql = "SELECT * FROM funcionario WHERE email = %s AND senha = %s"
        else:
            cursor.close()
            conn.close()
            return None  

        valores = (self.email, self.senha)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            self.id = resultado['id_aluno']
            self.email = resultado['email']
            return self
        else:
            return None

        
    

   

