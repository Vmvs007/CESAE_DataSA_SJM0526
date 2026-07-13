from BibliotecaMatematica import e_perfeito, e_primo, e_triangular
from BibliotecaPadroes import (
    imprimir_fibonacci,
    imprimir_potencias_de_dois,
    imprimir_triangulo_asteriscos,
    imprimir_triangulo_numerico,
)


def menu():
    print("1. Primo")
    print("2. Perfeito")
    print("3. Triangular")
    print("4. Fibonacci")
    print("5. Exponencial")
    print("6. Piramide Numerica")
    print("7. Piramide Asteriscos")
    print("0. Sair")


opcao = -1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        numero = int(input("Numero: "))
        print(e_primo(numero))
    elif opcao == 2:
        numero = int(input("Numero: "))
        print(e_perfeito(numero))
    elif opcao == 3:
        numero = int(input("Numero: "))
        print(e_triangular(numero))
    elif opcao == 4:
        quantidade = int(input("Quantidade: "))
        imprimir_fibonacci(quantidade)
    elif opcao == 5:
        quantidade = int(input("Quantidade: "))
        imprimir_potencias_de_dois(quantidade)
    elif opcao == 6:
        linhas = int(input("Linhas: "))
        imprimir_triangulo_numerico(linhas)
    elif opcao == 7:
        altura = int(input("Altura: "))
        imprimir_triangulo_asteriscos(altura)
    elif opcao == 0:
        print("Programa terminado")
    else:
        print("Opcao invalida")
