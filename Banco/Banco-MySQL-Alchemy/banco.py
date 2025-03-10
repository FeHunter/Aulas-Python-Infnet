from crud import *
from menu import *
from conectar_db import conectar

conn = conectar()
if (conn == None):
    print("Erro: problema com a conexão ao BD")
    exit()
opcao = entrar_opcao()
while (opcao != 0):
    match (opcao):
        case 1: incluir_conta()
        case 2: alterar_conta()
        case 3: excluir_conta()
        case 4: consultar_conta()
        case 5: consultar_contas()
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
