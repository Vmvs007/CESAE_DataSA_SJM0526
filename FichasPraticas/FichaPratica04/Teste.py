import numpy as np

vendas = np.array([100, 350, 600, 200, 90, 500, 2000, 2, 490, 220, 199, 590, 1950])

q1 = np.percentile(vendas, 25)
q3 = np.percentile(vendas, 75)

print(f"Q1: {q1}")
print(f"Q3: {q3}")

iqr = q3 - q1

print(f"IQR: {iqr}")

limiteInferior = q1 - 1.5 * iqr
limiteSuperior = q3 + 1.5 * iqr

print(f"Limite Inferior: {limiteInferior}")
print(f"Limite Superior: {limiteSuperior}")

outliers = vendas[(vendas < limiteInferior) | (vendas > limiteSuperior)]

print(outliers)
