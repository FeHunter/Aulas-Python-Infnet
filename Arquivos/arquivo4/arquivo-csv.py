import os, csv

NOME = 0
NOTA1 = 1
NOTA2 = 2
APROVACAO = 6

def definir_arquivo(nome_arquivo):
    dir_corrente = os.path.dirname(__file__)
    arquivo = os.path.join(dir_corrente, nome_arquivo)
    return arquivo

def ler_arquivo(arq):
    turma = []
    try:
        with open(arq, "r", encoding="UTF-8") as arquivo:
            turma_csv = csv.reader(arquivo, delimiter=";")
            next(turma_csv)
            for aluno in turma_csv:
                turma.append([aluno[NOME], float(aluno[NOTA1]), float(aluno[NOTA2])])
    except:
        print("Erro: abertura do arquivo")
        exit()
    return turma

def verificar_aprovacao(turma):
    aprovacao = []
    for aluno in turma:
        media = round((aluno[NOTA1] + aluno[NOTA2]) / 2, 1)
        if (media >= APROVACAO):
            aprovacao.append([aluno[NOME], media, "Aprovado"])
        else:
            aprovacao.append([aluno[NOME], media, "Prova final"])
    return aprovacao

def gravar_arquivo(arq, aprovacao):
    try:
        with open(arq, "w", encoding="UTF-8", newline="") as arquivo:
            aprovacao_csv = csv.writer(arquivo, delimiter=";")
            aprovacao_csv.writerow(["nome", "média", "status"])
            for aluno in aprovacao:
                aprovacao_csv.writerow(aluno)
            print("Arquivo gravado")
    except:
        print("Erro: gravação do arquivo")


arquivo_entrada = definir_arquivo("turma.csv")
turma = ler_arquivo(arquivo_entrada)
aprovacao = verificar_aprovacao(turma)
#print(aprovacao)
arquivo_saida = definir_arquivo("aprovacao.csv")
gravar_arquivo(arquivo_saida, aprovacao)