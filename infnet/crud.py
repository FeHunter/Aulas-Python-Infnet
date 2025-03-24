from conectar_db import *
from models import *

def incluir_aluno_endereco():
    aluno = Aluno("Felipe")
    aluno.endereco = Endereco("Rua do Felipe")
    try:
        session = conectar()
        session.add(aluno)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def incluir_emails():
    try:
        session = conectar()
        aluno = session.get(Aluno, 1)
        aluno.emails = [Email("felipe@gmail.com"), Email("felipe@infnet.br")]
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def incluir_disciplinas():
    try:
        session = conectar()
        disciplina = Disciplina("Python", 40)
        session.add(disciplina)
        disciplina = Disciplina("SQL", 40)
        session.add(disciplina)
        disciplina = Disciplina("PB", 20)
        session.add(disciplina)
        disciplina = Disciplina("C#", 20)
        session.add(disciplina)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def incluir_aluno_disciplina_1():
    try:
        session = conectar()
        session.add(AlunoDisciplina(1, 1))
        session.add(AlunoDisciplina(1, 2))
        session.add(AlunoDisciplina(1, 3))
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def incluir_aluno_disciplina_2():
    try:
        session = conectar()
        aluno = session.get(Aluno, 3)
        disciplina = session.get(Disciplina, 3)
        aluno.disciplinas.append(disciplina)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def excluir_aluno():
    aluno = consultar_aluno(1)
    try:
        session = conectar()
        session.delete(aluno)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def consultar_disciplina(id):
    try:
        session = conectar()
        disciplina = session.get(Disciplina, id)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return disciplina

def consultar_aluno(id):
    try:
        session = conectar()
        aluno = session.get(Aluno, id)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return aluno

def consultar_alunos():
    try:
        session = conectar()
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            print(aluno)
            if (aluno.endereco):
                print(aluno.endereco)
            for email in aluno.emails:
                print(email)
            for disciplina in aluno.disciplinas:
                print(disciplina)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def consultar_disciplinas():
    try:
        session = conectar()
        disciplinas = session.query(Disciplina).all()
        for disciplina in disciplinas:
            print(disciplina)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
