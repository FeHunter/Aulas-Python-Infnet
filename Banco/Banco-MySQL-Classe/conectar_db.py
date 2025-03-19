import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(user="root", password="hunter", database="banco")
        # print("BD conectado")
    except Exception as ex:
        print(f"Erro ao conectar: {ex}")
    return conn

def desconectar(conn):
    if (conn):
        conn.close()


