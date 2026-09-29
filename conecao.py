import psycopg2 as pg
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conexao():
    try:
        user = os.getenv('DB_USER')
        db = os.getenv('DB_DATABASE')
        pwd = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')

        print('Conectando ao banco, aguarde...')
        conect = pg.connect(
            user =  user,
            password = pwd,
            port = port,
            host = host,
            database = db
        )

        print('Conexão com o banco estabelecida.')
        return conect
    except Error as er:
        print(f'Ocorreu um erro ao se conectar ao banco: {er}')

def encerrar_conexao(conect):
    if conect:
        conect.close()
        print('Conexão com o banco encerrada.')