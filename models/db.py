import mysql.connector
from mysql.connector import Error       

def conectar():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password= '26032007',
            database = 'sistema_biblioteca'
        )
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    


