from models.db import conectar

class Emprestimo:

    def __init__(self, id_livro, data_emprestimo, data_devolucao, id_aluno, id_emprestimo=None):
        self.id = id_emprestimo
        self.id_livro = id_livro        
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao    
        self.id_aluno = id_aluno
        
    def salvar_emprestimos(self):
        conn = conectar()
        cursor = conn.cursor()
        
        if self.id is None:
     
            sql = """
            INSERT INTO emprestimos (id_livro,data_emprestimo,data_devolucao,id_aluno)
            VALUES (%s, %s, %s, %s)
            """
            valores = (self.id_livro,self.data_emprestimo,self.data_devolucao,self.id_aluno)

        else:
        
            sql = """
            UPDATE emprestimos
            SET id_livro = %s, data_emprestimo = %s, data_devolucao = %s, id_aluno = %s
            WHERE id_livro = %s
            """
                
            valores = (self.id_livro,self.data_emprestimo,self.data_devolucao,self.id_aluno)

            cursor.execute(sql, valores)
            conn.commit()

            cursor.close()
            conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM emprestimos")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Emprestimo(**r) for r in resultados]
    
    @staticmethod
    def buscar_por_id(id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
                        SELECT
                            l.titulo AS titulo,
                            e.data_emprestimo,
                            e.data_devolucao
                        FROM 
                            emprestimos e
                        JOIN 
                            livros l ON e.id_livro = l.id_livro
                        WHERE 
                            e.id_aluno = %s
                        """, (id,))


        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Emprestimo(**resultado) if resultado else None

    
    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM emprestimos WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def buscar_por_aluno(id_aluno):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM emprestimos WHERE id_aluno = %s", (id_aluno,))
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Emprestimo(**r) for r in resultados]