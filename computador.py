from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}"

    @abstractmethod
    def cadastrar(self):
        pass

