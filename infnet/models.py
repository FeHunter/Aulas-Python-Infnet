from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__= "aluno"

    id_aluno = Column(Integer, primary_key=True)
    nome_aluno = Column(String)
    endereco = relationship("Endereco", uselist=False)

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