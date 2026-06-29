import statistics as st

from docutils.parsers.rst.directives import percentage

notas = [8, 12, 15, 17, 9, 14, 18, 11, 13, 16, 7, 19, 10, 14, 15, 12, 14, 11, 15, 14, 14]

media = st.mean(notas)
mediana = st.median(notas)
maiorNota = max(notas)
menorNota = min(notas)
amplitude = maiorNota - menorNota

contadorAprovados = 0
contadorExcelentes = 0

for nota in notas:

    if nota >= 10:
        contadorAprovados += 1

    if nota >= 16:
        contadorExcelentes += 1

percentagemAprovados = (contadorAprovados / len(notas)) * 100
percentagemExcelentes = (contadorExcelentes / len(notas)) * 100

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Maior Nota: {maiorNota}")
print(f"Menor Nota: {menorNota}")
print(f"Amplitude: {amplitude}")
print(f"% de alunos aprovados: {percentagemAprovados}%")
print(f"% de alunos excelentes: {percentagemExcelentes}%")

print("____________________________________________")

desvioPadrao = st.stdev(notas)
print(f"Desvio Padrão: {desvioPadrao}")

contadorNotasDispersas = 0

for nota in notas:
    if nota < media - desvioPadrao or nota > media + desvioPadrao:
        contadorNotasDispersas += 1

contadorNotasMuitoDispersas = 0

for nota in notas:
    if nota < media - (2*desvioPadrao) or nota > media + (2*desvioPadrao):
        contadorNotasMuitoDispersas += 1

print(f"Notas fora do desvio padrão: {contadorNotasDispersas}/{len(notas)}")
print(f"Notas muito fora do desvio padrão: {contadorNotasMuitoDispersas}/{len(notas)}")
