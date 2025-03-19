from crud import *
from menu import *

opcao = entrar_opcao()
while (opcao != 0):
    match (opcao):
        case 1: incluir_conta()
        case 2: alterar_conta()
        case 3: excluir_conta()
        case 4: consultar_conta()
        case 5: consultar_contas()
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
