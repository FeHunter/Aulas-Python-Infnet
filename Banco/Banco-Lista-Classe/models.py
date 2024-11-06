class Conta():
    # construtor
    def __init__(self, id, nome, saldo): # o self é obrigatório e faz uma referência aos objetos da classe
        self.id = id
        self.nome = nome
        self.saldo = saldo
    
    def creditar(self, valor):
        self.saldo += valor
    
    def debitar(selft, valor):
        selft.saldo -= valor

    def __str__(self):
        return f"Nome: {self.nome} \nSaldo: {self.saldo}"
    
