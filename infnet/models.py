from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__= "aluno"

    id_aluno = Column(Integer, primary_key=True)
    nome_aluno = Column(String)
    endereco = relationship("Endereco", uselist=False)
    emails = relationship("Email")
    disciplinas = relationship("Disciplina", segundary="alunodisciplina", back_populates="alunos")

    def __init__(self, nome):
        self.nome_aluno = nome
    
    def __str__(self):
        return f"{self.id_aluno} {self.nome_aluno}"


class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True)
    rua = Column(String)
    id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"))
    aluno = relationship("Aluno", back_populates="endereco")

    def __init__(self, rua):
        self.rua = rua
    
    def __str__(self):
        return f"${self.id_endereco} {self.rua}"
    

class Email(Base):
    __tablename__ = "email"

    id_email = Column(Integer, primary_key=True)
    mail = Column(String)
    id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"))
    aluno = relationship("Aluno", back_populates="emails")

    def __init__(self, mail):
        self.mail = mail
    
    def __str__(self):
        return f"${self.id_email} {self.mail}"


class Disciplina(Base):
    __tablename__= "disciplina"

    id_disciplina = Column(Integer, primary_key=True)
    nome_disciplina = Column(String)
    creditos = Column(Integer)
    alunos = relationship("Alunos", segundary="alunodisciplina", back_populates="disciplinas")

    def __init__(self, nome, creditos):
        self.nome_disciplina = nome
        self.creditos = creditos
    
    def __str__(self):
        return f"{self.id_disciplina} {self.nome_disciplina} {self.creditos}"


class AlunoDisciplina ():
    __tablename__ = "alunodisciplina"
    
    id_aluno = Column(Integer, ForeignKey("aluno.id_aluno"), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey("disciplina.id_disciplina"), primary_key=True)

    def __init__(self, id_aluno, id_disciplina):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
    
    def __str__(self):
        return f"{self.id_aluno} {self.id_disciplina}"

