from enum import Enum


class ClasseAnimal(Enum):
    MAMIFERO = "Mamifero"
    ANFIBIO = "Anfibio"
    AVE = "Ave"
    PEIXE = "Peixe"
    REPTIL = "Reptil"


class Animal:
    def __init__(self, nome, especie, pais_origem, peso, alimentacao, classe_reino):
        self.__nome = nome
        self.__especie = especie
        self.__pais_origem = pais_origem
        self.__peso = peso
        self.__alimentacao = alimentacao
        self.__classe_reino = classe_reino

    def fazerBarulho(self):
        if self.__classe_reino == ClasseAnimal.MAMIFERO:
            print("Tinoninoni")
        elif self.__classe_reino == ClasseAnimal.ANFIBIO:
            print("Brrrrrr")
        elif self.__classe_reino == ClasseAnimal.AVE:
            print("Kwak Kwak")
        elif self.__classe_reino == ClasseAnimal.PEIXE:
            print("Blub Blub Splash")
        elif self.__classe_reino == ClasseAnimal.REPTIL:
            print("Psssssss")

    def comer(self, alimento, peso_gramas):
        if alimento in self.__alimentacao:
            self.__peso += peso_gramas / 1000
            print(f"O {self.__especie} {self.__nome} comeu {alimento}")
            self.fazerBarulho()
        else:
            print(f"O {self.__especie} {self.__nome} nao comeu {alimento}")

    def exibirDetalhes(self):
        print(f"{self.__especie} {self.__nome} | Origem: {self.__pais_origem} | Peso: {self.__peso:.2f} kg | Classe: {self.__classe_reino.value}")
