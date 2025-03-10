from conectar_db import *
import pandas as pd

APROVACAO = 6

def ler_turma():
    sql = "select * from aluno"
    try:
        engine = conectar()
        df_turma = pd.read_sql(sql, engine)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(engine)
    return df_turma

def verificar_aprovacao(df_turma):
    df_aprovacao = pd.DataFrame(columns=["nome", "média", "status"])
    for _, aluno in df_turma.iterrows():
        media = round((aluno["nota1"] + aluno["nota2"]) / 2, 1)
        if (media >= APROVACAO):
            df_aprovacao.loc[len(df_aprovacao)] = [aluno["nome"], media, "Aprovado"]
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno["nome"], media, "Prova final"]
    return df_aprovacao

def gravar_aprovacao(df_aprovacao):
    try:
        engine = conectar()
        df_aprovacao.to_sql("aprovacao", engine, if_exists="replace", index=False)
        print("Tabela gravada")
    except Exception as ex:
        print(ex)
    finally:
        desconectar(engine)


df_turma = ler_turma()
print(df_turma)
print(df_turma.dtypes)
df_aprovacao = verificar_aprovacao(df_turma)
print(df_aprovacao)
gravar_aprovacao(df_aprovacao)
