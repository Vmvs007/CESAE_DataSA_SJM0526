class Atleta:
    def __init__(self, nome, modalidade, altura, peso, pais_origem, ranking_mundial):
        self.__nome = nome
        self.__modalidade = modalidade
        self.__altura = altura
        self.__peso = peso
        self.__pais_origem = pais_origem
        self.__ranking_mundial = ranking_mundial

    def get_pais_origem(self):
        return self.__pais_origem

    def exibirDetalhes(self):
        print(f"{self.__nome} | {self.__modalidade} | {self.__altura} m | {self.__peso} kg | {self.__pais_origem} | Ranking: {self.__ranking_mundial}")
