from models.db import conectar

class Login:
    def _init_(self, email, senha, tipo):
        self.email = email
        self.senha = senha
        self.tipo = tipo

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
            print('Logado com sucesso!')
            return Login(email=resultado['email'], senha=resultado['senha'], tipo=self.tipo)
        else:
            return None

        
    

   

