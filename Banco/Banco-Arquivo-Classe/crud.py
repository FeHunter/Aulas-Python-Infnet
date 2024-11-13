from util import *
from models import Conta

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
        print("Erro: Conta não existe")
        return
    contas.remove(conta)

def alterar_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if not conta:
        print("Erro: Conta não existe")
        return
    oper = entrar_oper()
    valor = entrar_valor()
    if oper == "C":
        conta.creditar(valor)
    if oper == "D":
        conta.debitar(valor)
