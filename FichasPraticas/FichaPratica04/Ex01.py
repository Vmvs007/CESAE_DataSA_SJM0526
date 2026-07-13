import statistics as st


notas = [8, 12, 15, 17, 9, 14, 18, 11, 13, 16, 7, 19, 10, 14, 15, 12, 14, 11, 15, 14, 14]

media = st.mean(notas)
mediana = st.median(notas)
maior_nota = max(notas)
menor_nota = min(notas)
amplitude = maior_nota - menor_nota

aprovados = [nota for nota in notas if nota >= 10]
notas_16_ou_mais = [nota for nota in notas if nota >= 16]

percentagem_aprovados = len(aprovados) / len(notas) * 100
percentagem_16_ou_mais = len(notas_16_ou_mais) / len(notas) * 100

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Amplitude: {amplitude}")
print(f"Percentagem de alunos aprovados: {percentagem_aprovados:.2f}%")
print(f"Percentagem de alunos com nota >= 16: {percentagem_16_ou_mais:.2f}%")

print("\nInterpretacao:")
print("A media e a mediana estao proximas, por isso a media representa bem o desempenho geral.")
print("A diferenca entre a melhor e a pior nota e de 12 valores, mostrando alguma dispersao.")
print("Como a maior parte das notas se concentra entre 10 e 16, a turma tem desempenho razoavelmente homogeneo.")
