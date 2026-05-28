from FichaPratica02.Ex03.Retangulo import Retangulo

corUtilizador = input("Cor: ")

retangulo1 = Retangulo(cor=corUtilizador,
                       largura=int(input("Largura: ")),
                       altura=int(input("Altura: ")))

retangulo2 = Retangulo(cor="Verde", largura=35, altura=2)

print(f"Área: {retangulo1.area()}")
print(f"Perímetro: {retangulo1.perimetro()}\n")

print(f"Área: {retangulo2.area()}")
print(f"Perímetro: {retangulo2.perimetro()}\n")
