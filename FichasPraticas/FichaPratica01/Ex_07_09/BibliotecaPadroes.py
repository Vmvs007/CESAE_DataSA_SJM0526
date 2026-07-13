def imprimir_fibonacci(quantidade):
    if quantidade <= 0:
        print("Quantidade invalida")
        return

    sequencia = []
    primeiro = 0
    segundo = 1

    for _ in range(quantidade):
        sequencia.append(primeiro)
        primeiro, segundo = segundo, primeiro + segundo

    print(sequencia)


def imprimir_potencias_de_dois(quantidade):
    if quantidade <= 0:
        print("Quantidade invalida")
        return

    potencias = []

    for expoente in range(quantidade):
        potencias.append(2 ** expoente)

    print(potencias)


def imprimir_triangulo_numerico(linhas):
    if linhas <= 0:
        print("Numero de linhas invalido")
        return

    for linha in range(1, linhas + 1):
        for numero in range(1, linha + 1):
            print(numero, end=" ")
        print()


def imprimir_triangulo_asteriscos(altura):
    if altura <= 0:
        print("Altura invalida")
        return

    for linha in range(1, altura + 1):
        print("* " * linha)
