class Aluno():
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
    
    def calcular_media(self):
        media = (self.n1 + self.n2) / 2
        return media

    def __str__(self):
        return f"Nome: {self.nome}, Nota1: {self.n1}, Nota2: {self.n2}"