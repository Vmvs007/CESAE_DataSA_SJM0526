from Carro import Carro, TipoCombustivel


carro_a = Carro("Volkswagen", "Golf", "Branco", 1990, 90, 1600, TipoCombustivel.DIESEL, 6.5)
carro_b = Carro("Toyota", "Corolla", "Azul", 1988, 105, 1800, TipoCombustivel.GASOLINA, 7.2)
carro_c = Carro("BMW", "M3", "Preto", 2020, 480, 3000, TipoCombustivel.GASOLINA, 10.8)
carro_d = Carro("Peugeot", "308", "Cinzento", 2022, 130, 1500, TipoCombustivel.GPL, 6.0)

carros = [carro_a, carro_b, carro_c, carro_d]

for carro in carros:
    carro.exibirDetalhes()
    carro.ligar()
    print("__________________________")

vencedor_1 = carro_a.corrida(carro_b)
vencedor_2 = carro_c.corrida(carro_d)

print("Vencedor corrida A vs B:")
vencedor_1.exibirDetalhes()

print("Vencedor corrida C vs D:")
vencedor_2.exibirDetalhes()

vencedor_final = vencedor_1.corrida(vencedor_2)

print("Vencedor final:")
vencedor_final.exibirDetalhes()

consumo = vencedor_final.calcularConsumo(65)
print(f"Consumo numa viagem de 65 km: {consumo:.2f} litros")
