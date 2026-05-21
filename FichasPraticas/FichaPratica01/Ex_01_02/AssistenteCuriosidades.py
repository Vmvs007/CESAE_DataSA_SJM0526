from BibliotecaCuriosidades import *
from math import *


while True:
    
    numero = int(input("Coloca um numero: "))
    raiz = sqrt(numero)

    print("\n\n***** Assistente de Curiosidades *****")
    print("1. Maior de Idade")
    print("2. Fase da Vida")
    print("3. Capital Pais")
    print("4. Estação do Ano")
    print("5. Dia da Semana")
    print("6. Tipos de Números")

    print("0. Sair")

    opcao = int(input("Opção: "))

    if opcao==1 :
        print("\n** Maior de Idade **")
    
    elif opcao==2 :
        print("\n** Fase da Vida **")
    
    elif opcao==3 :
        print("\n** Capital País **")

        paisInput = input("País: ")

        capital = capital_pais(paisInput)

        print(capital)

        # print(capital_pais(paisInput))
    
    elif opcao==4 :
        print("\n** Estação do Ano **")

    elif opcao==5 :
        print("\n** Dia da Semana **")

    elif opcao==6 :
        print("\n** Tipos de Números **")
    
    elif opcao==0 :
        print("\n** Sair **")
        break

    else:
        print(f"\n** Opção não reconhecida: {opcao} **")