import sqlite3
import pathlib
import os

# Terminal › Integrated: Focus After Run e altera para terminal

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) + "\\banco.db"

def verificar_db():
    if (not os.path.exists(ARQ)):
        print("Erro: Banco de dados não existe")
        exit()

def conectar():
    conn = None
    try:
        conn = sqlite3.connect(ARQ)
    except Exception as ex:
        print(ex)
    return conn

def desconectar(conn):
    if (conn):
        conn.close()