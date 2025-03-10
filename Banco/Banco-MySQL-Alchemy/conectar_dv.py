import sqlite3
from models import Conta
import pathlib

# DIR_CURRENT = pathlib.Path(__file__).parent.resolve()
# ARQ = str(DIR_CURRENT)+"\\contas.csv"

ARQ = "C:\\Users\\hunte\\Downloads\\sqlite-tools-win-x64-3470000\\banco.db"

# conectar com o banco
try:
    conn = sqlite3.connect(ARQ)
    print("Banco conectado")
except Exception as ex:
    print(f"erro: {ex}")

# Conectar o curso ao banco conectado
cursor = conn.cursor()
# usa o curso para executar os comandos
cursor.execute("SELECT * FROM contas;")
# executa os comandos do curso e salvar na variavel registro
registros = cursor.fetchall()

contas = []

# pegar os registros do banco de dados e colocar na lista de contas
for registro in registros:
    contas.append(Conta(registro[0], registro[1], registro[2]))

for conta in contas:
    print(conta)

# fecha a conexão com o banco
conn.close()
