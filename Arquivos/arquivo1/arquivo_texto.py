import os

nome_arquivo = "nomes.txt"
dir_atual = os.path.dirname(__file__) # Pegar a pasta em que este programa esta
ARQ = os.path.join(dir_atual, nome_arquivo) #junta o nome do arquivo com o nome da pasta

def ler_arquivo_1():
    try:
        with open(ARQ, "r", encoding="UTF-8") as nomes:
            linha = nomes.readline()
            while (linha != ""):
                print(linha, end="")
                linha = nomes.readline()
    except:
        print("Erro: abertura do arquivo")

def ler_arquivo_2():
    try:
        with open(ARQ, "r", encoding="UTF-8") as nomes:
            while (linha := nomes.readline()):
                print(linha, end="")
                linha = nomes.readline()
    except:
        print("Erro: abertura do arquivo")

def ler_arquivo_3():
    try:
        with open(ARQ, "r", encoding="UTF-8") as nomes:
            for linha in nomes.readlines():
                print(linha, end="")
    except:
        print("Erro: abertura do arquivo")

def ler_arquivo_4():
    try:
        with open(ARQ, "r", encoding="UTF-8") as nomes:
            for linha in nomes:
                print(linha, end="")
    except:
        print("Erro: abertura do arquivo")

ler_arquivo_4()

