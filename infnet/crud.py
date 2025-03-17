from conectar_db import *
from models import *

def adicionar_aluno_endereco ():
    aluno = Aluno("Felipe")
    aluno.endereco = Endereco("Rua Barueri")
    try:
        session = conectar()
        session.add(aluno)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def consultar_alunos ():
    try:
        session = conectar()
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            print(aluno)
            print(aluno.endereco)
            for email in aluno.emails:
                print(email)
    except Exception as ex:
        print(f"Erro ao consultar alunos: {ex}")
    finally:
        desconectar(session)

def consultar_aluno(id):
    try:
        session = conectar()
        aluno = session.get(Aluno, id)
    except Exception as ex:
        print(f"Erro ao consultar aluno: {ex}")
    finally:
        desconectar(session)
    return aluno

def incluir_emails ():
    try:
        session = conectar()
        aluno = session.get(Aluno, 1)
        aluno.emails = [Email("felipe@gmail.com"), Email("felipe@infnet.br")]
        session.commit()
    except Exception as ex:
        print(f"Erro ao adicionar email: {ex}")
    finally:
        desconectar(session)

def incluir_disciplina ():
    try:
        session = conectar()
        disciplina = Disciplina("Python", 20)
        session.add(disciplina)
        disciplina = Disciplina("SQL", 40)
        session.add(disciplina)
        disciplina = Disciplina("PB", 20)
        session.add(disciplina)
        session.commit()
    except Exception as ex:
        print(f"Erro ao incluir disciplina: {ex}")
    finally:
        desconectar(session)

def consultar_disciplinas ():
    try:
        session = conectar()
        disciplinas = session.query(Disciplina).all()
        for disciplina in disciplinas:
            print(disciplina)
    except Exception as ex:
        print(f"Erro ao consultar disciplinas: {ex}")
    finally:
        desconectar(session) 