from ContaBancaria import ContaBancaria


conta1 = ContaBancaria("PT500001", "Ana Silva")
conta2 = ContaBancaria("PT500002", "Bruno Costa")
conta3 = ContaBancaria("PT500003", "Carla Mendes")

contas = [conta1, conta2, conta3]

conta1.depositar(1000)
conta2.depositar(250)
conta3.depositar(500)

conta1.levantar(300)
conta2.levantar(400)

conta2.transferencia(conta3, 1000)
conta1.transferencia(conta2, 200)

print("__________________________")

for conta in contas:
    conta.exibirDetalhes()
