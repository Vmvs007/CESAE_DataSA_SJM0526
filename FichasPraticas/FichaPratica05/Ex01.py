import numpy as np


temperaturas = np.array([
    18.5, 20.0, 21.3, 19.8, 22.1, 23.0, 24.5,
    25.2, 24.8, 23.5, 22.0, 21.7, 20.9, 19.5,
])

print("Temperaturas:")
print(temperaturas)
print(f"Shape: {temperaturas.shape}")
print(f"Tipo de dados: {temperaturas.dtype}")

media = np.mean(temperaturas)
minimo = np.min(temperaturas)
maximo = np.max(temperaturas)
amplitude = maximo - minimo
desvio_padrao = np.std(temperaturas)

print(f"Temperatura media: {media:.2f}")
print(f"Temperatura minima: {minimo:.2f}")
print(f"Temperatura maxima: {maximo:.2f}")
print(f"Amplitude termica: {amplitude:.2f}")
print(f"Desvio-padrao: {desvio_padrao:.2f}")

dias_superiores_media = np.where(temperaturas > media)[0]
dias_superiores_22 = temperaturas > 22

print(f"Dias com temperatura superior a media: {dias_superiores_media + 1}")
print(f"Temperaturas superiores a media: {temperaturas[dias_superiores_media]}")
print(f"Dias com temperatura superior a 22 graus: {np.sum(dias_superiores_22)}")
print(f"Percentagem acima de 22 graus: {np.mean(dias_superiores_22) * 100:.2f}%")

print("\nInterpretacao:")
print("A variacao e moderada: existe subida ate meio do periodo e depois uma descida gradual.")
