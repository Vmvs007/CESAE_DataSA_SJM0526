from enum import Enum


class TipoCombustivel(Enum):
    GASOLINA = "Gasolina"
    DIESEL = "Diesel"
    GPL = "GPL"


class Carro:
    def __init__(self, marca, modelo, cor, ano_fabrico, potencia, cilindrada, tipo_combustivel, consumo_litros_100_km):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano_fabrico = ano_fabrico
        self.__potencia = potencia
        self.__cilindrada = cilindrada
        self.__tipo_combustivel = tipo_combustivel
        self.__consumo_litros_100_km = consumo_litros_100_km

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_potencia(self):
        return self.__potencia

    def get_cilindrada(self):
        return self.__cilindrada

    def get_ano_fabrico(self):
        return self.__ano_fabrico

    def ligar(self):
        idade = 2025 - self.__ano_fabrico

        if idade > 30:
            if self.__tipo_combustivel == TipoCombustivel.DIESEL:
                print('"Deita um pouco de fumo... Custa a pegar... O carro esta ligado!"')
                print('"Vrum-vrum-vrum"')
            else:
                print('"Custa a pegar... O carro esta ligado!"')
                print('"Vrum-vrum-vrum"')
        else:
            if self.__potencia < 250:
                print('"O carro esta ligado!"')
                print('"Vruummmmmmmm"')
            else:
                print('"O carro esta ligado!"')
                print('"VRUUMMMMMMM"')

    def corrida(self, adversario):
        if self.__potencia > adversario.get_potencia():
            return self
        if self.__potencia < adversario.get_potencia():
            return adversario

        if self.__cilindrada > adversario.get_cilindrada():
            return self
        if self.__cilindrada < adversario.get_cilindrada():
            return adversario

        if self.__ano_fabrico > adversario.get_ano_fabrico():
            return self
        if self.__ano_fabrico < adversario.get_ano_fabrico():
            return adversario

        return None

    def calcularConsumo(self, distancia_km):
        return (self.__consumo_litros_100_km * distancia_km) / 100

    def exibirDetalhes(self):
        print(f"{self.__marca} {self.__modelo} | {self.__cor} | {self.__ano_fabrico} | {self.__potencia} cv | {self.__cilindrada} cc | {self.__tipo_combustivel.value}")
