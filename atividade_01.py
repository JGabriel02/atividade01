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

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Potência da Fonte: {self.__potenciaDaFonte}W"

    def cadastrar(self):
        pass

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Tempo de Bateria: {self.__tempoDeBateria}h"

    def cadastrar(self):
        pass


desktop = Desktop("Dell Inspiron", "Preto", 3500.0, 500)
notebook = Notebook("Lenovo Ideapad", "Prata", 2500.0, 8)

print(desktop.getInformacoes()) 
print(notebook.getInformacoes())
