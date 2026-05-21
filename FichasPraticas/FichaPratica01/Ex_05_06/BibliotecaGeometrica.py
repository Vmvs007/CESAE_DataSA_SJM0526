def pi():
    return 3.1415926


def area_quadrado(lado):
    area = lado * lado
    return area


def perimetro_quadrado(lado):
    perimetro = lado * 4
    return perimetro


def area_retangulo(base, altura):
    area = base * altura
    return area


def perimetro_retangulo(base, altura):
    perimetro = base + base + altura + altura
    return perimetro


def area_circulo(raio):
    area = pi() * (raio ** 2)
    return area


def perimetro_circulo(raio):
    perimetro = 2 * pi() * raio
    return perimetro
