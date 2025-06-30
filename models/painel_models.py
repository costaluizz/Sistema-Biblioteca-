from db import conectar

class Painel:
    def __init__(self,nome,livro,data_emprestimo,data_devolucao,id=None):
        self.id = id
        self.nome = nome
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def consultar_painel(self):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        

        
        
        
        cursor.execute(sql)
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        
        return resultados
     