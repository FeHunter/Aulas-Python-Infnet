from util import *

def exibir_menu ():
    print("[1] Incluir Conta")
    print("[2] Alterar Conta")
    print("[3] Excluir Conta")
    print("[4] Consultar conta")
    print("[5] Consultar Contas")
    print("[0] Sair")

def entrar_opcao():
    while True:
        exibir_menu()
        opcao = entrar_inteiro("Entrar Opção: ")
        if opcao < 0 or opcao > 5:
            print("Erro: Opção Inválida")
        else:
            break
    return opcao