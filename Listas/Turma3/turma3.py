from models import Aluno

MIN_TAMANHO_NOME = 2
FIM = 'fim'

def entrar_nome():
    while True:
        nome = input("Entre com o nome: ")
        if len(nome) >= MIN_TAMANHO_NOME:
            break
        else:
            print("Erro: nome inválido")
    return nome

def entrar_nota(msg):
    nota = 0
    while True:
        try:
            nota = float(input(msg))
            break
        except ValueError as e:
            print(f"Erro: Nota inválida : {e}")
    return nota

def entrar_alunos():
    turma = []
    nome = entrar_nome()
    while (nome.lower() != FIM):
        nota1 = entrar_nota("Entre com a nota 1: ")
        nota2 = entrar_nota("Entre com a nota 2: ")
        turma.append(Aluno(nome, nota1, nota2))
        nome = entrar_nome()
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


turma = entrar_alunos()
exibir_medias(turma)
exibir_aprovacao(turma)
