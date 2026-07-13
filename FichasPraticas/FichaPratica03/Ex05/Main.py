from Agenda import Agenda
from Pessoa import Pessoa


pessoa1 = Pessoa("Ana Silva", 22, "Porto", "ana@email.com", "910000001")
pessoa2 = Pessoa("Bruno Costa", 34, "Braga", "bruno@email.com", "910000002")
pessoa3 = Pessoa("Carla Mendes", 29, "Porto", "carla@email.com", "910000003")
pessoa4 = Pessoa("Diogo Santos", 41, "Lisboa", "diogo@email.com", "910000004")

agenda = Agenda(4)

agenda.adicionarPessoa(pessoa1)
agenda.adicionarPessoa(pessoa2)
agenda.listarContactos()

print("__________________________")

agenda.adicionarPessoa(pessoa3)
agenda.adicionarPessoa(pessoa4)
agenda.listarContactos()

print("__________________________")
agenda.pesquisarContactos("Porto")
