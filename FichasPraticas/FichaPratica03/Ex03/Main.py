from Animal import Animal, ClasseAnimal


animal = Animal("Simba", "Leao", "Tanzania", 180, ["carne", "frango"], ClasseAnimal.MAMIFERO)

animal.exibirDetalhes()
animal.fazerBarulho()

animal.comer("alface", 500)
animal.exibirDetalhes()

animal.comer("carne", 1200)
animal.exibirDetalhes()
