lista = [4, 5, 3, 7, 9, 1, 8, 2, 6, 10]

def pesquisar1(num, lista):
    achou = False
    for i in range(len(lista)):
        if (num == lista[i]):
            achou = True
            break
    return achou

def pesquisar2(num, lista):
    achou = False
    for i in lista:
        if (num == i):
            achou = True
            break
    return achou

num = 1
# achou = pesquisar1(num, lista)
# achou = pesquisar2(num, lista)
achou = num in lista
print("Encontrou: ",achou)