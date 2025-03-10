from conectar_db import *
from models import *

aluno = Aluno("Felipe")
aluno.endereco = Endereco("Rua Barueri")

try:
    session = conectar()
    session.add(aluno)
    session.commit()
except Exception as ex:
    print(ex)


