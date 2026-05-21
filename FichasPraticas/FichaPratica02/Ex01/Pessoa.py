class Pessoa:
    def __init__(self, nome="Joaquim", idade=25, altura=1.7):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura
