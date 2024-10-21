def separar_data (data):
    dia_mes_ano = data.split("/")
    dia = int(dia_mes_ano[0])
    mes = int(dia_mes_ano[1])
    ano = int(dia_mes_ano[2])
    return dia, mes, ano

def entrar_data():
    while (True):
        data = input("Entre com a data dd/mm/aaaa: ")
        if(len(data) != 10):
            print("erro: data inválida")
        else:
            break
    return data

def validar_data(dia, mes, ano):
    match mes:
        case 4 | 6 | 7 | 9 | 11:
            if ((dia >= 1) and (dia <= 30)):
                print("Data válida")
            else:
                print("Dia inválido")
        case 1 | 3 | 5 | 8 | 10 | 12:
            if ((dia >= 1) and (dia <= 31)):
                print("Data válida")
            else:
                print("Dia inválido")
        case 2:
            if ((ano % 4) == 0):
                if ((dia >= 1) and (dia <= 29)):
                    print("Data válida")
                else:
                    print("Dia inválido")
            else:
                if ((dia >= 1) and (dia <= 28)):
                    print("Data válida")
                else:
                    print("Dia inválido")
        case _:
            print("Mês inválido")

# Main
data = entrar_data()
dia, mes, ano = separar_data(data)
validar_data(dia, mes, ano)


