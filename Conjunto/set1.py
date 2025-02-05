c1 = {1, 1, 3, 3, 5, 5}

print("Conjunto 1")
print(c1)
c1.add(0) # adicionar
print(c1)
c1.remove(3) # removers
print(c1)

print("\nConjunto 2")
c2 = {1, 2, 5, 7}
print(c2)

print("\nOperações")
c3 = c1 & c2 # interseção de dois conjuntos
# c3 = c1.intersection(c2)
print(c3)

c3 = c1 | c2 # união
# c3.union(c2)
print(c3)

c3 = c1 - c2 # diferença
# c3 = c1.difference(c2)
print(c3)
