def media_aluno(notas1, notas2):
    medias = []
    for nota1, nota2 in zip(notas1, notas2):
        soma = nota1 + nota2
        media = soma / 2
        medias.append(media)
    return medias

def exibir_alunos_medias(nomes, medias):
    for nome, media in zip(nomes, medias):
        print(f"Aluno: {nome} - Media: {media}")

def exibir_aprovados_reprovados(nomes, medias):
    print("\nAlunos aprovados:")
    for nome, media in zip(nomes, medias):
        if media >= 6:
            print(f"{nome} - Aprovado")
        else:
            print(f"{nome} - Reprovado")

def entrar_nome():
    return input("Digite o nome do aluno: ")

def entrar_nota(msg):
    return float(input(msg))

def entrar_nomes_notas():
    nomes = []
    notas1 = []
    notas2 = []
    nome = entrar_nome()
    while nome.lower() != 'fim':
        nota1 = entrar_nota("Entre com a 1° nota: ")
        nota2 = entrar_nota("Entre com a 2° nota: ")
        nomes.append(nome)
        notas1.append(nota1)
        notas2.append(nota2)
        nome = entrar_nome()
    return nomes, notas1, notas2


nomes, notas1, notas2 = entrar_nomes_notas()
medias = media_aluno(notas1, notas2)
print("\nMédias calculadas:")
print(medias)
exibir_alunos_medias(nomes, medias)
exibir_aprovados_reprovados(nomes, medias)
