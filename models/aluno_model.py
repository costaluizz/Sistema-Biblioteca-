from db import conectar
class Aluno:
    def __init__(self, nome, email, senha,id=None):
        self.nome = nome
        self.email = email
        self.senha = senha

    def salvar_aluno(self):
        conn = conectar()
        cursor = conn.cursor()
        
        if self.id is None:  
            sql = """
            INSERT INTO alunos (nome, email,senha)
            VALUES (%s, %s)
            """
            valores = (self.nome,self.email,self.senha)
        else: 
            sql = """
            UPDATE alunos
            SET nome = %s, email = %s, senha = %s
            WHERE email = %s
            """
            valores = (self.nome,self.email,self.senha,self.id)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM alunos")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Aluno(**r) for r in resultados]
    
    @staticmethod
    def buscar_por_id(id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM alunos WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Aluno(**resultado) if resultado else None
        
     
    def deletar(self):
         if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alunos WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()
                    
                