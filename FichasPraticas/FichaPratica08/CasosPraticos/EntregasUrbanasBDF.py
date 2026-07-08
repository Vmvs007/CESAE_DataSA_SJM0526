# ============================================================
# Caso prático de regressão — Entregas urbanas
# Objetivo: prever o tempo de entrega em minutos
# ============================================================

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# 1. Criar o conjunto de dados
# ============================================================

# Para obter sempre os mesmos dados
np.random.seed(42)

# Número de entregas
n = 300

# Criar dados simulados
distancia = np.random.randint(1, 21, n)          # distância entre 1 e 20 km
numero_paragens = np.random.randint(1, 9, n)    # entre 1 e 8 paragens
peso = np.round(np.random.uniform(0.5, 15, n), 1)  # peso entre 0.5 kg e 15 kg
transito = np.random.randint(1, 10, n)          # trânsito entre 1 e 9

# Criar o tempo de entrega com uma relação lógica
tempo_entrega = (
    distancia * 3.2 +
    numero_paragens * 2.5 +
    peso * 0.8 +
    transito * 3 +
    np.random.normal(0, 4, n)
)

# Arredondar e garantir que não existem tempos negativos
tempo_entrega = np.round(tempo_entrega).astype(int)
tempo_entrega = np.maximum(tempo_entrega, 5)

# Criar DataFrame
df = pd.DataFrame({
    "Distancia_km": distancia,
    "Numero_Paragens": numero_paragens,
    "Peso_kg": peso,
    "Transito": transito,
    "Tempo_Entrega_Min": tempo_entrega
})

print(df.head())
print(df.shape)


# ============================================================
# 2. Explorar rapidamente os dados
# ============================================================

print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nInformações do DataFrame:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nValores em falta por coluna:")
print(df.isnull().sum())


# ============================================================
# 3. Definir variáveis independentes e variável alvo
# ============================================================

X = df[["Distancia_km", "Numero_Paragens", "Peso_kg", "Transito"]]

y = df["Tempo_Entrega_Min"]


# ============================================================
# 4. Separar dados em treino e teste
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nTamanho dos dados de treino:")
print(X_train.shape)

print("\nTamanho dos dados de teste:")
print(X_test.shape)


# ============================================================
# 5. Criar e treinar o modelo de regressão linear
# ============================================================

modelo = LinearRegression()

modelo.fit(X_train, y_train)


# ============================================================
# 6. Consultar coeficientes do modelo
# ============================================================

print("\nCoeficientes do modelo:")

coeficientes = pd.DataFrame({
    "Variavel": X.columns,
    "Coeficiente": modelo.coef_
})

print(coeficientes)

print("\nIntercepto:")
print(modelo.intercept_)


# ============================================================
# 7. Fazer previsões com os dados de teste
# ============================================================

previsoes = modelo.predict(X_test)

print("\nPrevisões realizadas:")
print(previsoes)


# ============================================================
# 8. Avaliar o modelo
# ============================================================

mae = mean_absolute_error(y_test, previsoes)
r2 = r2_score(y_test, previsoes)

print("\nAvaliação do modelo:")
print("MAE:", round(mae, 2))
print("R²:", round(r2, 2))


# ============================================================
# 9. Comparar valores reais com valores previstos
# ============================================================

resultado = pd.DataFrame({
    "Real": y_test.values,
    "Previsto": previsoes
})

resultado["Previsto"] = resultado["Previsto"].round(1)

print("\nComparação entre valores reais e previstos:")
print(resultado)


# ============================================================
# 10. Adicionar coluna com erro
# ============================================================

resultado["Erro"] = resultado["Real"] - resultado["Previsto"]

print("\nComparação com erro:")
print(resultado)


# ============================================================
# 11. Fazer uma previsão para uma nova entrega
# ============================================================

nova_entrega = pd.DataFrame({
    "Distancia_km": [6],
    "Numero_Paragens": [3],
    "Peso_kg": [4.5],
    "Transito": [5]
})

previsao_nova_entrega = modelo.predict(nova_entrega)

print("\nPrevisão para uma nova entrega:")
print("Tempo previsto:", round(previsao_nova_entrega[0], 1), "minutos")