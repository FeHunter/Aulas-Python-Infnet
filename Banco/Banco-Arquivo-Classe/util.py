def entrar_inteiro(msg):
    while (True):
        try:
            num = int(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return num

def entrar_real(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except:
            print("Erro: Valoar inválido")
    return num

def entrar_id():
    while (True):
        id = entrar_inteiro("Entre com o id da conta: ")
        if (id <= 0):
            print("Erro: id inválido")
        else:
            break
    return id

def entrar_nome():
    while (True):
        nome = input("Entre com o nome: ")
        if (len(nome) < 2):
            print("Erro: nome inválido")
        else:
            break
    return nome

def entrar_saldo():
    while (True):
        saldo = entrar_real("Entre com o saldo: ")
        if (saldo < 0):
            print("Erro: saldo menor do que zero")
        else:
            break
    return saldo

def pesquisar_id(contas, id):
    conta_pesquisada = []
    for conta in contas:
        if (conta.id == id):
            conta_pesquisada = conta
            break
    return conta_pesquisada

def entrar_oper():
    oper = ''
    while True:
        oper = input("[C]Crédito | [D]Débito: ").upper()
        if oper not in ("C", "D"):
            print("Erro: operação inválida")
        else:
            break
    return oper

def entrar_valor():
    valor = 0
    while True:
        valor = entrar_real("Entre com o valor: ")
        if valor > 0:
            break
    return valor
