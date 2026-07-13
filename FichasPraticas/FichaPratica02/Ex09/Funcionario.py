class Funcionario:
    def __init__(self, nome, email, departamento, salario):
        self.__nome = nome
        self.__email = email
        self.__departamento = departamento
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_departamento(self):
        return self.__departamento

    def get_salario(self):
        return self.__salario

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def aumentarSalario(self, percentagem):
        self.__salario += self.__salario * (percentagem / 100)

    def exibirDetalhes(self):
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Departamento: {self.__departamento}")
        print(f"Salario: {self.__salario:.2f} EUR")
