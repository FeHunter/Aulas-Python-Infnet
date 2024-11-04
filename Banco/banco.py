from crud import *
from menu import *

contas = [[1, "Cassio", 100], [2, "Patrick", 200], [3, "Rafael", 300], [4, "Felipe", 400]]

exibir_menu()
op = int(input("Entrar opção: "))
while op != 0:
    exibir_menu()
    match op:
        case 1: incluir_conta(contas)
        case 2: alterar_conta(contas)
        case 3: excluir_conta(contas)
        case 4: consultar_conta(contas)
        case 5: consultar_contas(contas)
        case _: print("Erro: opção inválida")
    op = int(input("Entrar opção: "))

#incluir_conta(contas)
consultar_contas(contas)
# excluir_conta(contas)
alterar_conta(contas)
consultar_contas(contas) # mostra alterações feitas
