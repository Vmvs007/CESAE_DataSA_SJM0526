from enum import Enum


class TipoImovel(Enum):
    APARTAMENTO = "Apartamento"
    CASA = "Casa"
    MANSAO = "Mansao"


class Acabamento(Enum):
    PARA_RESTAURO = "Para restauro"
    USADA = "Usada"
    NOVA = "Nova"
    NOVA_COM_ALTO_ACABAMENTO = "Nova com alto acabamento"


class Imovel:
    def __init__(self, rua, numero_porta, cidade, tipo, acabamento, area_total, numero_quartos, numero_casas_banho, area_piscina):
        self.__rua = rua
        self.__numero_porta = numero_porta
        self.__cidade = cidade
        self.__tipo = tipo
        self.__acabamento = acabamento
        self.__area_total = area_total
        self.__numero_quartos = numero_quartos
        self.__numero_casas_banho = numero_casas_banho
        self.__area_piscina = area_piscina

    def set_acabamento(self, acabamento):
        self.__acabamento = acabamento

    def calcularValor(self):
        if self.__tipo == TipoImovel.APARTAMENTO:
            valor = self.__area_total * 1000
        elif self.__tipo == TipoImovel.CASA:
            valor = self.__area_total * 3000
        else:
            valor = self.__area_total * 5000

        if self.__acabamento == Acabamento.PARA_RESTAURO:
            valor *= 0.5
        elif self.__acabamento == Acabamento.USADA:
            valor *= 0.9
        elif self.__acabamento == Acabamento.NOVA_COM_ALTO_ACABAMENTO:
            valor *= 1.25

        valor += self.__numero_quartos * 7500
        valor += self.__numero_casas_banho * 10500
        valor += self.__area_piscina * 1000

        return valor

    def compararImoveis(self, outro_imovel):
        if self.calcularValor() >= outro_imovel.calcularValor():
            return self
        return outro_imovel

    def exibirDetalhes(self):
        print(f"{self.__tipo.value} em {self.__cidade}, {self.__rua} n. {self.__numero_porta}")
        print(f"Acabamento: {self.__acabamento.value}")
        print(f"Area: {self.__area_total} m2 | Quartos: {self.__numero_quartos} | WC: {self.__numero_casas_banho} | Piscina: {self.__area_piscina} m2")
        print(f"Valor: {self.calcularValor():.2f} EUR")
