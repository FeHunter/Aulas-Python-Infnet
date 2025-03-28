import os
import pandas as pd

APROVACAO = 6

def definir_arquivo (nome_arquivo):
    dir_corrente = os.path.dirname(__file__)
    arquivo = os.path.join(dir_corrente, nome_arquivo)
    return arquivo

def ler_arquivo (arq):
    df_turma = None
    try:
        df_turma = pd.read_csv(arq, sep=";", encoding="UTF-8")
    except:
        print("Erro ao abrir o arquivo")
        exit()
    return df_turma

def verificar_aprovacao (df_turma):
    df_aprovacao = pd.DataFrame(columns=["Nome", "Média", "Status"])
    for _, aluno in df_turma.iterrows():
        media = round((aluno['nota1'] + aluno['nota2']) / 2, 1)
        if (media >= APROVACAO):
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, "Aprovado"]
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, "Prova Final"]
    return df_aprovacao

def gravar_arquivo (arq, df_aprovacao):
    try:
        df_aprovacao.to_csv(arq, sep=";", index=False)
    except:
        print("Erro ao gravar o arquivo")


arq = definir_arquivo("turma.csv")
df_turma = ler_arquivo(arq)
print(df_turma)
df_aprovacao =  verificar_aprovacao(df_turma)
print(df_aprovacao)
arq = definir_arquivo("aprovacao.csv")
gravar_arquivo(arq, df_aprovacao)