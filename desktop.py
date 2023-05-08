from computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Potência da Fonte: {self.__potenciaDaFonte}W"

    def cadastrar(self):
        pass