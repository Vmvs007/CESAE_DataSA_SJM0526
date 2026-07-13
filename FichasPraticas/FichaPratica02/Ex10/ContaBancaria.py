class ContaBancaria:
    def __init__(self, iban, titular):
        self.__iban = iban
        self.__titular = titular
        self.__saldo = 0

    def get_iban(self):
        return self.__iban

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Deposito recusado. Valor invalido.")
            return

        self.__saldo += valor
        print(f"{valor:.2f} EUR depositados na conta {self.__iban}")

    def levantar(self, valor):
        if valor <= 0:
            print("Levantamento recusado. Valor invalido.")
        elif self.__saldo >= valor:
            self.__saldo -= valor
            print(f"{valor:.2f} EUR levantados da conta {self.__iban}")
        else:
            print(f"Saldo insuficiente na conta {self.__iban}. Levantamento de {valor:.2f} EUR recusado.")

    def transferencia(self, conta_destino, valor):
        if valor <= 0:
            print("Transferencia recusada. Valor invalido.")
        elif self.__saldo >= valor:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            print(f"{valor:.2f} EUR transferidos da conta {self.__iban} para a conta {conta_destino.get_iban()}")
        else:
            print(f"Saldo insuficiente na conta {self.__iban}. Transferencia de {valor:.2f} EUR para a conta {conta_destino.get_iban()} recusada.")

    def exibirDetalhes(self):
        print(f"IBAN: {self.__iban} | Titular: {self.__titular} | Saldo: {self.__saldo:.2f} EUR")
