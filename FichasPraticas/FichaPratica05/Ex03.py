import numpy as np

notas = np.array([
    [12.2, 15, 14],
    [8.5, 10, 9],
    [17.9, 18, 16],
    [14, 13, 15],
    [10, 11, 12]
])

print(notas)
print(f"\nShape: {notas.shape}")

print(f"\nMédia geral: {np.mean(notas)}")
print(f"Média por aluno: {np.round(np.mean(notas, axis=1), 2)}")
print(f"Média por teste: {np.mean(notas, axis=0)}")

print(f"\nMelhor nota por aluno: {np.max(notas, axis=1)}")
print(f"  Pior nota por aluno: {np.min(notas, axis=1)}")

notasNegativas=np.where(notas<10)
# print(f"Notas Negativas: {notasNegativas}")
print(f"\nNotas Negativas: {notas[notasNegativas]}")
print(f"Quantidade Notas Negativas: {len(notas[notasNegativas])}")