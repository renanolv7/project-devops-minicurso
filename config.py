from mysql.connector import connect, Error
import os
from dotenv import load_dotenv

load_dotenv()

def connect_bd():
    try:
        config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }
        conn = connect(**config)
        print("Conectado ao banco com sucesso!")
        return conn
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None


# Esse arquivo, em específico, contém uma função para tentativa de conexão ao banco de dados em nuvem da Azure.
# As credenciais do banco estão sendo inacessiveis, pois estamos utilizando dotenv para não expor.
# Mais explicações se encontram em README.md