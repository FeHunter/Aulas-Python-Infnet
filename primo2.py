def verificar_primo (num):
    primo = True
    div = 2
    while (primo and (div < num - 1)):
        if ((num % div) == 0):
            primo = True
            break
        else:
            div += 1
    return primo
    
def entrar_limite_inferior ():
    while (True):
        num = int(input("Entre com o limite inferior: "))
        if (num <= 0):
            print("Erro: número inválido")
        else:
            break
    return num

def entrar_limite_superior (limite_inferior):
    while (True):
        num = int(input("Entre com o limite superior: "))
        if (num < limite_inferior):
            print("Erro: limite superior deve ser maior ou igual ao inferior")
        else:
            break
    return num

def mostrar_primo (num, primo):
    if (primo): 
        print(num , "é primo")
    else:
        print(num , "não é primo")


# num = entrar_numero()
FIM = 0
limite_inferior = entrar_limite_inferior()
limite_superior = entrar_limite_superior(limite_inferior)

for num in range(limite_inferior, limite_superior + 1):
    primo = verificar_primo(num)
    mostrar_primo(num, primo)

