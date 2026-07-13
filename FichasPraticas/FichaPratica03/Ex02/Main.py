from ContaBancaria import ContaBancaria


conta1 = ContaBancaria("PT900001", "Ana Silva")
conta2 = ContaBancaria("PT900002", "Bruno Costa")
conta3 = ContaBancaria("PT900003", "Carla Mendes")

conta1.depositar(1000)
conta2.depositar(300)
conta3.depositar(800)

conta2.pedirEmprestimo(500)
conta1.pedirEmprestimo(400)
conta1.pedirEmprestimo(100)
conta1.amortizarEmprestimo(900)
conta1.amortizarEmprestimo(200)

print("__________________________")

for conta in [conta1, conta2, conta3]:
    conta.exibirDetalhes()
