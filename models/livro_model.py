from db import conectar

def inserir_livro(titulo, autor, editora, ano, quantidade_disponivel,status='disponível'):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = """
    INSERT INTO livros (titulo, autor, editora, ano, quantidade_disponivel, status)
    VALUES (%s, %s, %s, %s, %s,  %s)

    """

    valores = (titulo, autor, editora, ano, quantidade_disponivel,status)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

def atualizar_livro(id, titulo, autor, editora, ano, quantidade_disponivel,status):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = """
    UPDATE livros
    SET titulo = %s, autor = %s, editora = %s, ano = %s, quantidade_disponivel = %s, status = %s
    WHERE id = %s
    """
    
    valores = (titulo, autor, editora, ano, quantidade_disponivel,status, id)
    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

def excluir_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = """
    DELETE FROM livros
    WHERE id = %s
    """
    
    cursor.execute(sql, (id,))
    conn.commit()

    cursor.close()
    conn.close()