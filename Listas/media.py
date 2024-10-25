def entrar_numeros():
    numeros = []
    num = int(input("Digite uma sequencia de numeros, para finalizar digite 0: "))
    while (num != 0):
        numeros.append(num)
        num = int(input("Digite uma sequencia de numeros, para finalizar digite 0: "))
    return numeros

def calc_soma(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

def calc_medi(soma, numeros):
    media = (soma / len(numeros))
    return media

def selecionar_numeros(nuns, med):
    selecionados = []
    for num in nuns:
        if (num >= med):
            selecionados.append(num)
    return selecionados

def mostrar_numeros(nums):
    print(nums)


numeros = entrar_numeros()
soma = calc_soma(numeros)
media = calc_medi(soma, numeros)
print(f"Soma: {soma}, Media: {media}")
nums_maior_que_media = selecionar_numeros(numeros, media)
mostrar_numeros(nums_maior_que_media)