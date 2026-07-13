import numpy as np


notas = np.array([
    [12, 15, 14],
    [8, 10, 9],
    [17, 18, 16],
    [14, 13, 15],
    [10, 11, 12],
])

print("Matriz das notas:")
print(notas)
print(f"Shape: {notas.shape}")

media_aluno = np.mean(notas, axis=1)
media_teste = np.mean(notas, axis=0)
melhor_nota_aluno = np.max(notas, axis=1)
pior_nota_aluno = np.min(notas, axis=1)
media_geral = np.mean(notas)
notas_negativas = notas[notas < 10]

print(f"Media de cada aluno: {np.round(media_aluno, 2)}")
print(f"Media de cada teste: {np.round(media_teste, 2)}")
print(f"Melhor nota de cada aluno: {melhor_nota_aluno}")
print(f"Pior nota de cada aluno: {pior_nota_aluno}")
print(f"Media geral da turma: {media_geral:.2f}")
print(f"Notas negativas: {notas_negativas}")
print(f"Quantidade de notas negativas: {len(notas_negativas)}")

melhor_teste = np.argmax(media_teste) + 1
print("\nInterpretacao:")
print(f"A turma teve melhor desempenho no teste {melhor_teste}.")
