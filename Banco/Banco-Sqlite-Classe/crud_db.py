from conectar_db import *
from models import Conta

def consultar_contas_db():
    comando = "select * from contas;"
    contas = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            contas.append(Conta(registro[0], registro[1], registro[2]))
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return contas

def consultar_conta_db(id):
    comando = "select * from contas where id = ?;"
    conta = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (id,))
        registro = cursor.fetchall()
        if (registro):
            conta = Conta(registro[0][0], registro[0][1], registro[0][2])
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return conta

def incluir_conta_db(conta):
    comando = "INSERT INTO contas (nome, saldo) VALUES (?, ?);"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.nome, conta.saldo))
        conn.commit()
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        desconectar(conn)

def excluir_conta_db(conta):
    comando = "DELETE FROM contas WHERE id == ?;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.id,))
        conn.commit()
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        desconectar(conn)

def alterar_conta_db(conta):
    comando = "UPDATE contas SET saldo == ? WHERE id == ?;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.saldo, conta.id))
        conn.commit()
    except Exception as ex:
        print(f"Erro: {ex}")
    finally:
        desconectar(conn)