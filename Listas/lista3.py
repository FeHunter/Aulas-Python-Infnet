lista1 = [4, 5, 3, 7, 9]
lista2 = [1, 8, 2, 6, 10]
lista = lista1 + lista2
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

print(min(lista))
print(max(lista))
print(sum(lista))