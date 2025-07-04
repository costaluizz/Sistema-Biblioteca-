from db import conectar

class Livro:
    def __init__(self, titulo, autor, editora, ano ,id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
   
    def salvar_livro(self):
        conn = conectar()
        cursor = conn.cursor()
        
        if self.id is None:
            sql = """
            INSERT INTO livros (titulo, autor, editora, ano)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (self.titulo, self.autor, self.editora, self.ano)
        else:
            sql = """
            UPDATE livros
            SET titulo = %s, autor = %s, editora = %s, ano = %s
            WHERE id = %s
            """
            valores = (self.titulo, self.autor, self.editora, self.ano,self.id)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM livros")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Livro(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM livros WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Livro(**resultado) if resultado else None



    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM livros WHERE id = %s",(self.id,))
            conn.commit()
            cursor.close()
            conn.close()