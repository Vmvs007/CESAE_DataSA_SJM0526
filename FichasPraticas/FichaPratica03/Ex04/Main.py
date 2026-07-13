from Imovel import Acabamento, Imovel, TipoImovel


imovel1 = Imovel("Rua das Flores", 10, "Porto", TipoImovel.APARTAMENTO, Acabamento.USADA, 95, 3, 2, 0)
imovel2 = Imovel("Avenida Central", 5, "Lisboa", TipoImovel.CASA, Acabamento.NOVA_COM_ALTO_ACABAMENTO, 210, 4, 3, 25)

imovel_mais_caro = imovel1.compararImoveis(imovel2)

print("Imovel mais caro:")
imovel_mais_caro.exibirDetalhes()
