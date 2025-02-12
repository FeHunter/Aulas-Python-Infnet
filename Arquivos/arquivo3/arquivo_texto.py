import os

nome_arquivo = "nomes.txt"
dir_atual = os.path.dirname(__file__) # Pegar a pasta em que este programa esta
ARQ = os.path.join(dir_atual, nome_arquivo) #junta o nome do arquivo com o nome da pasta

def ler_arquivo():
    nomes = []
    try:
        with open(ARQ, "r", encoding="UTF-8") as arq:
            for linha in arq:
                linha = linha.strip("\n")
                nomes.append(linha)
    except:
        print("Erro: abertura do arquivo")
        exit()

    return nomes

def converter_nomes (nomes):
    nomes_convertidos = []
    for nome in nomes:
        nome_sobrenome = nome.split(" ")
        tam = len(nome_sobrenome)
        nomes_convertidos.append(f"{nome_sobrenome[tam-1].upper()}, {nome_sobrenome[0].lower()}")
    return nomes_convertidos

def gravar_arquivos (nomes):
    try:
        with open(ARQ, 'w', encoding="UTF-8") as arq:
            for nome in nomes:
                arq.write(f"{nome}\n")
            print("Arquivo salvo com sucesso!")
    except:
        print("Erro ao salvar o arquivo")


nomes = ler_arquivo()
nomes = converter_nomes(nomes)
print(nomes)
gravar_arquivos(nomes)