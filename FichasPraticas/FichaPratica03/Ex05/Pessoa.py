class Pessoa:
    def __init__(self, nome, idade, cidade, email, telemovel):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade
        self.__email = email
        self.__telemovel = telemovel

    def get_cidade(self):
        return self.__cidade

    def exibirDetalhes(self):
        print(f"{self.__nome} | {self.__idade} anos | {self.__cidade} | {self.__email} | {self.__telemovel}")
