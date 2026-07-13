from Atleta import Atleta
from Competicao import Competicao


atleta1 = Atleta("Ana Silva", "Atletismo", 1.68, 58, "Portugal", 12)
atleta2 = Atleta("Bruno Costa", "Natacao", 1.82, 76, "Brasil", 8)
atleta3 = Atleta("Carla Mendes", "Tenis", 1.70, 62, "Portugal", 20)
atleta4 = Atleta("Diogo Santos", "Ciclismo", 1.78, 70, "Espanha", 15)
atleta5 = Atleta("Eva Martins", "Judo", 1.65, 60, "Franca", 5)
atleta6 = Atleta("Fabio Rocha", "Atletismo", 1.85, 78, "Portugal", 3)

competicao1 = Competicao("Meeting Porto", "Portugal", 4)
competicao2 = Competicao("Open Madrid", "Espanha", 4)

competicao1.inscreverAtleta(atleta1)
competicao1.inscreverAtleta(atleta2)
competicao1.inscreverAtleta(atleta3)

competicao2.inscreverAtleta(atleta4)
competicao2.inscreverAtleta(atleta5)
competicao2.inscreverAtleta(atleta6)

competicao1.listarParticipantes()
competicao1.atletasDaCasa()

print("__________________________")

competicao2.listarParticipantes()
competicao2.atletasDaCasa()
