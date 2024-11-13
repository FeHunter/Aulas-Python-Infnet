from models import Aluno
import pathlib

def ler_turma():
    dir_current = pathlib.Path(__file__).parent.resolve()
    file = str(dir_current)+"\\turma.csv"
    turma = []
    try:
        with(open(file, "r") as file):
            linha = file.readline()
            while linha := file.readline() :
                linha = linha.strip("\n").split(",")
                nome, n1, n2 = linha[0], float(linha[1]), float(linha[2])
                turma.append(Aluno(nome, n1, n2))
    except:
        print("Erro: Leitura do arqvuivo csv")
    return turma

def exibir_turma(turma):
    for aluno in turma:
        print(aluno)
    print()

def exibir_medias(turma):
    for aluno in turma:
        media = aluno.calcular_media()
        print(f"Nome: {aluno.nome}, Média: {media}")

def exibir_aprovacao(turma):
    for aluno in turma:
        media = aluno.calcular_media()
        if media >= 6:
            print(f"{aluno.nome} Aprovado")
        else:
            print(f"{aluno.nome} Prova Final")


turma = ler_turma()
exibir_medias(turma)
exibir_aprovacao(turma)
