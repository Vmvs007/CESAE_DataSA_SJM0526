from BibliotecaGeometrica import *

while True:

    print("\n\n***** Calculadora Geométrica *****")
    print("1. Área do Quadrado")
    print("2. Perímetro do Quadrado")
    print("3. Área do Retângulo")
    print("4. Perímetro do Retângulo")
    print("5. Área do Círculo")
    print("6. Perímetro do Círculo")
    print("7. Área do Triângulo")

    print("0. Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print("\n** Área do Quadrado **")

        lado_quadrado = float(input("Insira o lado (m.): "))
        print(f"{area_quadrado(lado_quadrado)} m2")

        # print(area_quadrado(lado_quadrado),"m2")

    elif opcao == 2:
        print("\n** Perímetro do Quadrado **")

    elif opcao == 3:
        print("\n** Área do Retângulo **")

        base_retangulo = float(input("Base do Retângulo (m.): "))
        altura_retangulo = float(input("Altura do Retângulo (m.): "))

        resultado = area_retangulo(altura=altura_retangulo,base=base_retangulo)
        # Mesma coisa: resultado = area_retangulo(base_retangulo, altura_retangulo)

        print(f"{resultado} m2")

    elif opcao == 4:
        print("\n** Perímetro do Retângulo **")

    elif opcao == 5:
        print("\n** Área do Círculo **")

    elif opcao == 6:
        print("\n** Perímetro do Círculo **")

    elif opcao == 7:
        print("\n** Área do Triângulo **")

    elif opcao == 0:
        print("\n** Sair **")
        break

    else:
        print(f"\n** Opção não reconhecida: {opcao} **")
