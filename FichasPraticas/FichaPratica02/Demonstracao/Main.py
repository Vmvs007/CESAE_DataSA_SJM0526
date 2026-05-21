from FichaPratica02.Demonstracao.Carro import Carro

carro1 = Carro(marca="Fiat", modelo="500", cor="Vermelho", preco=15000, kms=50000)
carro2 = Carro(marca="Honda", modelo="Civic", cor="Amarelo", preco=7500, kms=200000)

carro1.ligar()
carro2.buzinar()

carro1.marca="Ferrari"
carro1.buzinar()
