import mysql.connector
from mysql.connector import Error       

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password= '26032007',
            database = 'sistema_biblioteca'
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
conexao = conectar()


