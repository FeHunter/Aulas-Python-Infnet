import os, csv

nome_arquivo = "turma.csv"
dir_atual = os.path.dirname(__file__) # Pegar a pasta em que este programa esta
ARQ = os.path.join(dir_atual, nome_arquivo) #junta o nome do arquivo com o nome da pasta

# Posição index para valores da turma
NOME = 0
NOTA1 = 1
NOTA2 = 2

def ler_arquivo():
    turma = []
    try:
        with open(ARQ, "r") as arq:
            turma_csv = csv.reader(arq, delimiter=";")
            next(turma_csv) # Pular a primeira linha do arquivo
            for aluno in turma_csv:
                turma.append([aluno[NOME], float(aluno[NOTA1]), float(aluno[NOTA2])])
    except:
        print("Erro: abertura do arquivo")
        exit()

    return turma

def gravar_arquivos (turma):
    try:
        with open(ARQ, 'w', encoding="UTF-8") as arq:
            for nome in turma:
                arq.write(f"{nome}\n")
            print("Arquivo salvo com sucesso!")
    except:
        print("Erro ao salvar o arquivo")


turma = ler_arquivo()
print(turma)
# gravar_arquivos(turma)