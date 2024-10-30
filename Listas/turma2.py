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
        turma.append([nome, nota1, nota2])
        nome = entrar_nome()
    return turma

def exibir_turma(turma):
    for aluno in turma:
        for info_aluno in aluno:
            print(info_aluno, end=" ")
        print()

def calcular_medias(turma):
    medias = []
    for aluno in turma:
        soma_notas = aluno[1] + aluno[2]
        media = soma_notas / 2
        medias.append([aluno[0], media])
    return medias

def exibir_medias(medias):
    for media in medias:
        print(f"Nome: {media[0]}, Média: {media[1]}")

def exibir_aprovacao(medias):
    for media in medias:
        if media[1] >= 6:
            print(f"{media[0]} Aprovado")
        else:
            print(f"{media[0]} Reprovado")


# turma = [["Felipe", 6.5, 7.5], ["Patrick", 7, 6], ["Rafael", 5, 8], ["Cassio", 6, 8]]
turma = entrar_alunos()
# exibir_turma(turma)
medias = calcular_medias(turma)
exibir_medias(medias)
exibir_aprovacao(medias)
