from FichaPratica02.Ex08.Produto import Produto

produto1 = Produto("Coca-cola",1.5)
produto2 = Produto("Bolachas",2.99)
produto3 = Produto("Azeite",6.50)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()

print("\n___________________________________\n")

produto1.adquirirStock(15)
produto2.adquirirStock(100)
produto3.adquirirStock(25)
produto3.adquirirStock(12)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()

print("\n___________________________________\n")

produto1.vender(10)
produto2.vender(250)

produto1.exibirDetalhes()
produto2.exibirDetalhes()
produto3.exibirDetalhes()