from util import *

def consultar_contas(contas):
    for conta in contas:
        print(conta[0], conta[1], conta[2])

def consultar_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    print(conta[0], conta[1], conta[2])
      
def incluir_conta(contas):
    id = entrar_id()
    conta = pesquisar_id(contas, id)
    if (conta):  #(conta != []):
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    conta = [id, nome, saldo]
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
    novoSaldo = entrar_valor()
    if oper == "C":
        conta[2] += novoSaldo
    if oper == "D":
        conta[2] -= novoSaldo