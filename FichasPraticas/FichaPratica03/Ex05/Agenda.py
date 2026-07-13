class Agenda:
    def __init__(self, tamanho_lista):
        self.__ano_criacao = 2025
        self.__lista_contactos = []
        self.__tamanho_lista = tamanho_lista

    def adicionarPessoa(self, pessoa):
        if len(self.__lista_contactos) < self.__tamanho_lista:
            self.__lista_contactos.append(pessoa)
            print("Pessoa adicionada com sucesso.")
        else:
            print("Agenda cheia.")

    def listarContactos(self):
        print(f"Agenda criada em {self.__ano_criacao}")

        for pessoa in self.__lista_contactos:
            pessoa.exibirDetalhes()

    def pesquisarContactos(self, cidade_pesquisa):
        print(f"Contactos em {cidade_pesquisa}:")

        for pessoa in self.__lista_contactos:
            if pessoa.get_cidade().lower() == cidade_pesquisa.lower():
                pessoa.exibirDetalhes()
