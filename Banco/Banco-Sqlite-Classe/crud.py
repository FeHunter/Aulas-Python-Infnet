from util import *
from models import *

def consultar_contas(contas):
    for conta in contas:
        print(conta)

def consultar_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    print(conta)
    
def incluir_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (conta):  #(conta != []):
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    conta = Conta(id, nome, saldo)
    contas.append(conta)

def excluir_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    contas.remove(conta)

def alterar_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta.creditar(valor)
    else:
        conta.debitar(valor)
