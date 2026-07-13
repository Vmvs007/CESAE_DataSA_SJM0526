class Aluno:
    def __init__(self, nome, idade, email, curso, media):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__curso = curso
        self.__media = media

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

    def get_curso(self):
        return self.__curso

    def get_media(self):
        return self.__media

    def set_curso(self, curso):
        self.__curso = curso

    def set_media(self, media):
        self.__media = media

    def felizAniversario(self):
        self.__idade += 1

    def situacaoAprovacao(self):
        return self.__media > 9.5

    def exibirDetalhes(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Email: {self.__email}")
        print(f"Curso: {self.__curso}")
        print(f"Media: {self.__media}")
