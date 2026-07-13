from Funcionario import Funcionario


funcionario = Funcionario("Carla Mendes", "carla@email.com", "Financeiro", 1200)

funcionario.exibirDetalhes()
print("__________________________")

funcionario.aumentarSalario(15)
funcionario.exibirDetalhes()
