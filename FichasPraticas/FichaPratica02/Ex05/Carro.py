class Carro:
    def __init__(self, marca, modelo, cor, ano_fabrico):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano_fabrico = ano_fabrico

    def ligar(self):
        print(f"O {self.__marca} {self.__cor} está ligado...")
