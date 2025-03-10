from conectar_db import *
import pandas as pd

APROVACAO = 6

def ler_turma(banco):
    sql = "select * from aluno"
    try:
        engine = conectar(banco)
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

def gravar_aprovacao(banco, df_aprovacao):
    try:
        engine = conectar(banco)
        df_aprovacao.to_sql("aprovacao", engine, if_exists="replace", index=False)
        print("Tabela gravada")
    except Exception as ex:
        print(ex)
    finally:
        desconectar(engine)

banco = definir_banco("turma.db")
verificar_banco(banco)
df_turma = ler_turma(banco)
print(df_turma)
print(df_turma.dtypes)
df_aprovacao = verificar_aprovacao(df_turma)
print(df_aprovacao)
gravar_aprovacao(banco, df_aprovacao)
