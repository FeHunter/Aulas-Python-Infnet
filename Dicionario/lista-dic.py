#benchmark dicionário python

import time

TAM = 100_000
#TAM = 101
ID = TAM - 1

def criar_lista():
    lista = []
    for i in range(1, TAM):
        produto = [i, "Produto " + str(i), i]
        lista.append(produto)
    return lista

def pesquisar_lista(lista, id):
    for produto in lista:
        if (produto[0] == id):
            return produto
    return None

def criar_dic():
    dic = {}
    for i in range(1, TAM):
        dic[i] = ["Produto " + str(i), i]
    return dic

def pesquisar_dic(dic, id):
    return dic[id]

'''
lista = criar_lista()
inicio = time.process_time()
produto = pesquisar_lista(lista, ID)
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)
lista.clear()
'''

dic = criar_dic()
#print(dic)
inicio = time.process_time()
produto = pesquisar_dic(dic, ID)
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)
