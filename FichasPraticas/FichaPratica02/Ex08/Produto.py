class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
        self.__stock = 0

    def adquirirStock(self, quantidade):
        self.__stock += quantidade

    def vender(self, quantidade):

        if (self.__stock >= quantidade):
            self.__stock -= quantidade
            print(f"Venda de {self.__nome} efetuada")
        else:
            print(f"Venda de {self.__nome} recusada. Ruptura de stock.")

    def exibirDetalhes(self):
        print(f"{self.__nome} | {self.__preco} € | Stock: {self.__stock}")
