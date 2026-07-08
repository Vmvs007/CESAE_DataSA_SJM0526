# ============================================================
# Caso prático de regressão — Entregas urbanas
# Objetivo: prever o tempo de entrega em minutos
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# 1. Criar o conjunto de dados
# ============================================================

dados = {
    "Distancia_km": [2, 4, 6, 8, 10, 3, 7, 12, 15, 5, 9, 11, 14, 1, 13],
    "Numero_Paragens": [1, 2, 3, 4, 5, 1, 3, 6, 7, 2, 4, 5, 6, 1, 6],
    "Peso_kg": [1.5, 3.0, 2.5, 5.0, 7.0, 2.0, 4.0, 8.0, 10.0, 3.5, 6.0, 7.5, 9.0, 1.0, 8.5],
    "Transito": [2, 3, 4, 5, 7, 2, 5, 8, 9, 3, 6, 7, 8, 1, 8],
    "Tempo_Entrega_Min": [10, 18, 27, 38, 52, 14, 35, 65, 80, 22, 48, 58, 74, 7, 70]
}

df = pd.DataFrame(dados)


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
    test_size=0.15,
    random_state=42
)

print("\nTamanho dos dados de treino:")
print(X_train.shape)

print("\nTamanho dos dados de teste:")
print(X_test.shape)


# ============================================================
# 5. Criar e treinar o modelo de regressão linear
# ============================================================
print("\nModelo vai começar a treinar agora")

modelo = LinearRegression()

modelo.fit(X_train, y_train)

print("\nModelo Treinado\n")


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