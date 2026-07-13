class Competicao:
    def __init__(self, nome, pais, numero_maximo_inscritos):
        self.__nome = nome
        self.__pais = pais
        self.__participantes = []
        self.__numero_maximo_inscritos = numero_maximo_inscritos

    def inscreverAtleta(self, atleta):
        if len(self.__participantes) < self.__numero_maximo_inscritos:
            self.__participantes.append(atleta)
            print("Atleta inscrito com sucesso.")
        else:
            print("Competicao sem vagas.")

    def listarParticipantes(self):
        print(f"Participantes da competicao {self.__nome}:")

        for atleta in self.__participantes:
            atleta.exibirDetalhes()

    def atletasDaCasa(self):
        print(f"Atletas da casa em {self.__nome}:")

        for atleta in self.__participantes:
            if atleta.get_pais_origem().lower() == self.__pais.lower():
                atleta.exibirDetalhes()
