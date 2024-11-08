# pode usar aspas '' ou ""
nome = "felipe"

#pode ser acessar os elementos da string
print(nome[0]) 
print(nome[1])

# string são imutaveis, não pode ser alterado atravas dos elementos
#nome[0] = nome[0].upper()
# caso precise alterar uma string você pode atribuir os valores em novo string
novo_nome = nome[0].upper() + '...'
novo_nome = f"{novo_nome} 9"
novo_nome = novo_nome + str(10)

# você pode acessar os ultimo elementos da string usando números negativos
ultimo = nome[-1]
print(f"Ultimo: {ultimo}")

# remover algo da string do início ou do final da string
nome_stripe = nome.strip("pe")

print(nome_stripe)
print(nome)
print(novo_nome)

# converte string para numero, e usando replace para mudar , por .
string_num = "103,94"
# string_num.replace(",", ".")
# num_ = float(string_num)
print(string_num)

# string_num = "100, 50, 30, 25, 43"
# string_num.replace(',', '.')
# nums = float(string_num)
# print(nums)

# [inicio:fim:incremento]
string_num_2 = "0123456789"
print(string_num_2[0:10:2])

