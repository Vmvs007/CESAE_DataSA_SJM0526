class Edificio:
    def __init__(self, nome="Edificio Genérico", rua="Rua Genérica", cidade="Porto", cor_fachada="Branca",
                 num_andares=1, tem_garagem=False):
        self.__nome = nome
        self.__rua = rua
        self.__cidade = cidade
        self.__cor_fachada = cor_fachada
        self.__num_andares = num_andares
        self.__tem_garagem = tem_garagem

    def get_nome(self):
        return self.__nome

    def get_rua(self):
        return self.__rua

    def get_cidade(self):
        return self.__cidade

    def get_cor_fachada(self):
        return self.__cor_fachada

    def get_num_andares(self):
        return self.__num_andares

    def get_tem_garagem(self):
        return self.__tem_garagem

    def set_cor_fachada(self, cor_fachada):
        self.__cor_fachada = cor_fachada
