class Retangulo:
    def __init__(self, cor, largura, altura):
        self.__cor = cor
        self.__largura = largura
        self.__altura = altura

    def area(self):
        resultado = self.__largura * self.__altura
        return resultado

    def perimetro(self):
        resultado = (self.__largura + self.__altura) * 2
        return resultado
