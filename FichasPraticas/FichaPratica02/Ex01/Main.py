from FichaPratica02.Ex01.Pessoa import Pessoa

pessoa1 = Pessoa(nome="Vitor",idade=26,altura=1.75)
pessoa2 = Pessoa()


print(f"{pessoa1.get_nome()} {pessoa1.get_idade()} {pessoa1.get_altura()}")

print(f"{pessoa2.get_nome()} {pessoa2.get_idade()} {pessoa2.get_altura()}")