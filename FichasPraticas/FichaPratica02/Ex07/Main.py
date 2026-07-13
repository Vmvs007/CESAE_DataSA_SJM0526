from Aluno import Aluno


aluno1 = Aluno("Ana Silva", 22, "ana@email.com", "Python", 15)
aluno2 = Aluno("Bruno Costa", 24, "bruno@email.com", "Python", 7.5)

alunos = [aluno1, aluno2]

for aluno in alunos:
    aluno.exibirDetalhes()

    if aluno.situacaoAprovacao():
        print("Situacao: Aprovado")
    else:
        print("Situacao: Reprovado")

    print("__________________________")
