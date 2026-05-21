from BibliotecaConversoes import *

print("**** Conversor de Euros para outras moedas ****")

euros = float(input("Euros: "))
moedaPretendida = input("Que moeda queres? (USD | GBP | BRL | ...): ")

quantidadePessoas=int(input("Por quantas pessoas queres dividir o valor convertido: "))

valorConvertido = converter_moedas(euros,moedaPretendida)/quantidadePessoas

if valorConvertido<0:
    print("Moeda não encontrada")
else:
    print(f"Cada pessoa fica com {valorConvertido} {moedaPretendida}")
