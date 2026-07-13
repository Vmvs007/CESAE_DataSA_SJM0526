import statistics as st


tempos = [4, 6, 5, 7, 12, 3, 4, 5, 20, 6, 7, 5, 4, 30, 6, 8, 5, 2, 4, 12, 6]

media = st.mean(tempos)
mediana = st.median(tempos)
maior_tempo = max(tempos)
menor_tempo = min(tempos)
amplitude = maior_tempo - menor_tempo
desvio_padrao = st.stdev(tempos)
tempos_acima_media = [tempo for tempo in tempos if tempo > media]
tempos_acima_10 = [tempo for tempo in tempos if tempo > 10]
valores_extremos = [tempo for tempo in tempos if tempo > 15]

print(f"Media: {media:.2f} minutos")
print(f"Mediana: {mediana} minutos")
print(f"Maior tempo: {maior_tempo} minutos")
print(f"Menor tempo: {menor_tempo} minutos")
print(f"Amplitude: {amplitude} minutos")
print(f"Desvio-padrao: {desvio_padrao:.2f}")
print(f"Chamadas acima da media: {len(tempos_acima_media)}")
print(f"Chamadas acima de 10 minutos: {len(tempos_acima_10)}")
print(f"Possiveis valores extremos: {valores_extremos}")

print("\nInterpretacao:")
print("A media e afetada pelos atendimentos muito longos, especialmente 20 e 30 minutos.")
print("A mediana representa melhor o tempo tipico, porque fica menos influenciada por extremos.")
print("O servico parece eficiente na maioria das chamadas, mas deve investigar os casos acima de 15 minutos.")
