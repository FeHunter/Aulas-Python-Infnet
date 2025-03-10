import os
from sqlalchemy import create_engine

def definir_banco(nome_banco):
    dir_corrente = os.path.dirname(__file__)
    banco = os.path.join(dir_corrente, nome_banco)
    banco = banco.replace("\\", "\\\\")
    return banco

def verificar_banco(banco):
    if (not os.path.exists(banco)):
        print("Erro: banco não existe")
        exit()

def conectar(banco):
    try:
        engine = create_engine("sqlite:///" + banco)
    except Exception as ex:
        print(ex)
    return engine

def desconectar(engine):
    if (engine):
        engine.dispose()
