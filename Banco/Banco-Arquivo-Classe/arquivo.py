from models import Conta
import pathlib

DIR_CURRENT = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CURRENT)+"\\contas.csv"

def ler_conta():
    conta = []
    try:
        with(open(ARQ, "r", encoding="UTF-8") as arquivo):
            while linha := arquivo.readline() :
                campos = linha.strip("\n").split(",")
                id, nome, saldo = int(campos[0]), campos[1], float(campos[2])
                conta.append(Conta(id, nome, saldo))
    except:
        print("Erro: Leitura do arqvuivo csv")
    return conta

def gravar_contas(contas):
    try:
        with(open (ARQ, "w", encoding="UTF-8") as arquivo):
            for conta in contas:
                arquivo.write(f"{conta.id},{conta.nome},{conta.saldo}\n")
    except:
        print("Erro: Ao salvar do arqvuivo csv")