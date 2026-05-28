class Livro:
    def __init__(self, titulo, autor, categoria, num_paginas, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
        self.__num_paginas = num_paginas
        self.__isbn = isbn

    def exibir_detalhes(self):
        print(f"{self.__titulo} | {self.__categoria} | {self.__autor}")
        print(f"Núm. Páginas: {self.__num_paginas} | {self.__isbn}")
