import sys

def entrar_numero():
    num = int(input("Entre com o número: "))
    return num

def calcular_media(soma, cont):
    media = soma / cont
    print("Media = ", media)

FIM = 0
soma = cont = 0
maior = -sys.maxsize - 1
menor = sys.maxsize
num = entrar_numero()

while (num != FIM):
    soma += num
    cont += 1
    if (num > maior):
        maior = num
    if (num < menor):
        menor = num

    num = entrar_numero()

if (cont != 0):
    print("Soma = ", soma)
    calcular_media(soma, cont)
    print("Maior = ", maior)
    print("Menor = ", menor)
