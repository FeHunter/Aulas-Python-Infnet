def verificar_primo (num):
    primo = True
    div = 2
    while (primo and (div < num - 1)):
        if (num % div == 0):
            primo = True
        else:
            div += 1
        return primo
    
def verificar_primo_for (num):
    primo = True
    for div in range(2, num):
        if (num % div == 0):
            primo = True
            break
    return primo

def entrar_numero ():
    while (True):
        num = int(input("Entre com o número positivo: "))
        if (num < 0):
            print("Erro: número inválido")
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
num = entrar_numero()
while (num != FIM):
    primo = verificar_primo(num)
    mostrar_primo(num, primo)
    num = entrar_numero()

