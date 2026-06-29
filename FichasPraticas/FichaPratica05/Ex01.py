import numpy as np

temperaturas = np.array([
    18.5, 20.0, 21.3, 19.8, 22.1, 23.0, 24.5, 25.2, 24.8, 23.5, 22.0, 21.7, 20.9, 19.5
])

print(f"Shape: {temperaturas.shape}")
print(f"Data Type: {temperaturas.dtype}")

print(f"\nTemp. Média: {np.mean(temperaturas)}")
print(f"Temp. Min: {np.min(temperaturas)}")
print(f"Temp. Max: {np.max(temperaturas)}")
print(f"Amplitude: {np.max(temperaturas) - np.min(temperaturas)}")
print(f"Desvio Padrão: {np.std(temperaturas)}")

diasAcimaMedia = np.where(temperaturas > np.mean(temperaturas))

print(f"\nIndex dias acima da média: {diasAcimaMedia[0]}")
print(f"Temperaturas dos dias acima da média {temperaturas[diasAcimaMedia[0]]}")

diasAcima22C = temperaturas > 22
quantidadeDiasAcima22C = sum(diasAcima22C)
print(f"\nDias acima de 22ºC: {quantidadeDiasAcima22C}")

# diasAcima22C = np.where(temperaturas > 22)
# print(len(diasAcima22C[0]))

percentagemDiasAcima22C = quantidadeDiasAcima22C / len(temperaturas) * 100
print(f"Percentagem dias acima de 22ºC: {percentagemDiasAcima22C}%")
