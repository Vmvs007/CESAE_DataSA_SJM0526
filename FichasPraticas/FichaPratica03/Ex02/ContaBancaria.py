class ContaBancaria:
    def __init__(self, iban, titular):
        self.__iban = iban
        self.__titular = titular
        self.__saldo = 0
        self.__ano_abertura = 2025
        self.__margem_emprestimo = 0.5
        self.__valor_divida = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"{valor:.2f} EUR depositados na conta {self.__iban}")

    def pedirEmprestimo(self, valor):
        limite = self.__saldo * self.__margem_emprestimo

        if self.__valor_divida > 0:
            print("Emprestimo recusado: existe divida ativa.")
        elif valor > limite:
            print("Emprestimo recusado: valor acima da margem permitida.")
        else:
            self.__saldo += valor
            self.__valor_divida += valor
            print(f"Emprestimo de {valor:.2f} EUR concedido.")

    def amortizarEmprestimo(self, valor):
        if valor > self.__valor_divida:
            print("Amortizacao recusada: valor superior ao valor em divida.")
        elif valor > self.__saldo:
            print("Amortizacao recusada: saldo insuficiente.")
        else:
            self.__saldo -= valor
            self.__valor_divida -= valor
            print(f"Amortizacao de {valor:.2f} EUR efetuada.")

    def exibirDetalhes(self):
        print(f"IBAN: {self.__iban} | Titular: {self.__titular} | Ano: {self.__ano_abertura} | Saldo: {self.__saldo:.2f} EUR | Divida: {self.__valor_divida:.2f} EUR")
