from util import *
from models import *
from crud_db import *

def consultar_contas():
    contas = consultar_contas_db()
    for conta in contas:
        print(conta)

def consultar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não existe")
        return
    print(conta)
    
def incluir_conta():
    nome = entrar_nome()
    saldo = entrar_saldo()
    conta = Conta(id, nome, saldo)
    incluir_conta_db(conta)

def excluir_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não existe")
        return
    excluir_conta_db(conta)

def alterar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta.creditar(valor)
    else:
        conta.debitar(valor)
    alterar_conta_db(conta)
