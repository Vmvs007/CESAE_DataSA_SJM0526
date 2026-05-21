class Carro:

    def __init__(self, marca="Opel", modelo="Corsa", cor="Branco", preco=1500, kms=350000):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.kms = kms

    def buzinar(self):
        print(f"Buzina do {self.marca} {self.cor}: BEEP!")

    def ligar(self):
        print(f"{self.marca} {self.cor} ligou: VRUMMMM! VRUMMMM!")