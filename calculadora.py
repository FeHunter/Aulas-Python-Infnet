def exibir_menu():
    print("----Menu----")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    print("[0] - Sair")

def entrar_operacao():
    while True:
        exibir_menu()
        oper = int(input("Entre com a operação: "))
        if (oper < 0 or oper > 4):
            print('Erro: operação inválida')
        else:
            break
    return oper

def entrar_operando():
    op = float(input("Entre com o operando: "))
    return op

def somar(op1, op2):
    result = op1 + op2
    print("Soma =", result)

def subtrair(op1, op2):
    result = op1 - op2
    print("Subtração =", result)

def multiplicar(op1, op2):
    result = op1 * op2
    print("Multiplicação =", result)

def dividir(op1, op2):
    if (op2 != 0):
        result = op1 / op2
        print("Divisão =", result)
    else:
        print("Erro: divisão por zero")

def executar_operaca (oper, op1, op2):
    match (oper):
        case 1:
            somar(op1, op2)
        case 2:
            subtrair(op1, op2)
        case 3:
            multiplicar(op1, op2)
        case 4:
            dividir(op1, op2)
        case _:
            print("Erro: operação inválida")

# Main
FIM = 0
oper = entrar_operacao()
while (oper != FIM):
    op1 = entrar_operando()
    op2 = entrar_operando()
    executar_operaca(oper, op1, op2)
    oper = entrar_operacao()

