import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


dados = {
    "Temperatura_C": [21, 23, 25, 29, 31, 22, 27, 33, 24, 30, 20, 26, 32, 28, 35, 22, 24, 29, 34, 36, 21, 25, 27, 31, 33, 23, 28, 30, 37, 26],
    "Humidade_Percentagem": [45, 48, 52, 60, 68, 46, 55, 72, 50, 65, 44, 53, 70, 58, 76, 47, 49, 62, 74, 80, 43, 51, 56, 69, 73, 48, 59, 66, 82, 54],
    "Consumo_kWh": [120, 135, 150, 190, 230, 125, 175, 260, 145, 220, 115, 165, 250, 185, 280, 130, 140, 200, 270, 300, 118, 155, 170, 240, 265, 138, 188, 225, 320, 160],
    "Alertas_24h": [1, 2, 3, 7, 10, 1, 5, 14, 2, 9, 0, 4, 12, 6, 16, 1, 2, 8, 15, 18, 0, 3, 5, 11, 13, 2, 6, 9, 20, 4],
    "Dias_Desde_Manutencao": [10, 18, 25, 45, 60, 12, 35, 80, 22, 55, 8, 30, 75, 40, 90, 15, 20, 50, 85, 100, 9, 28, 33, 65, 78, 19, 42, 58, 110, 31],
    "Falhas_Ultimos_30_Dias": [0, 0, 1, 2, 3, 0, 1, 4, 0, 3, 0, 1, 4, 2, 5, 0, 0, 2, 4, 6, 0, 1, 1, 3, 4, 0, 2, 3, 7, 1],
    "Servidores_Ativos": [20, 24, 28, 35, 42, 22, 32, 48, 26, 40, 18, 30, 45, 34, 52, 23, 25, 38, 50, 55, 19, 29, 31, 44, 47, 27, 36, 41, 60, 30],
    "Nivel_Risco": ["Baixo", "Baixo", "Medio", "Medio", "Alto", "Baixo", "Medio", "Alto", "Baixo", "Alto", "Baixo", "Medio", "Alto", "Medio", "Alto", "Baixo", "Baixo", "Medio", "Alto", "Alto", "Baixo", "Medio", "Medio", "Alto", "Alto", "Baixo", "Medio", "Alto", "Alto", "Medio"],
}

df_servidores = pd.DataFrame(dados)

print("Primeiras linhas:")
print(df_servidores.head())
print("\nInfo:")
df_servidores.info()
print("\nEstatisticas descritivas:")
print(df_servidores.describe())
print("\nValores em falta:")
print(df_servidores.isnull().sum())
print("\nClasses:")
print(df_servidores["Nivel_Risco"].value_counts())

print("\nTemperatura media por risco:")
print(df_servidores.groupby("Nivel_Risco")["Temperatura_C"].mean())
print("\nConsumo medio por risco:")
print(df_servidores.groupby("Nivel_Risco")["Consumo_kWh"].mean())
print("\nAlertas medios por risco:")
print(df_servidores.groupby("Nivel_Risco")["Alertas_24h"].mean())
print("\nFalhas medias por risco:")
print(df_servidores.groupby("Nivel_Risco")["Falhas_Ultimos_30_Dias"].mean())

df_servidores["Nivel_Risco"].value_counts().plot(kind="bar")
plt.title("Contagem de salas por nivel de risco")
plt.xlabel("Nivel de risco")
plt.ylabel("Numero de salas")
plt.tight_layout()
plt.show()

df_servidores.groupby("Nivel_Risco")["Alertas_24h"].mean().plot(kind="bar")
plt.title("Media de alertas por risco")
plt.xlabel("Nivel de risco")
plt.ylabel("Alertas 24h")
plt.tight_layout()
plt.show()

cores = df_servidores["Nivel_Risco"].map({"Baixo": "green", "Medio": "orange", "Alto": "red"})
plt.figure(figsize=(7, 4))
plt.scatter(df_servidores["Temperatura_C"], df_servidores["Consumo_kWh"], c=cores)
plt.xlabel("Temperatura")
plt.ylabel("Consumo kWh")
plt.title("Temperatura vs Consumo por risco")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
plt.scatter(df_servidores["Dias_Desde_Manutencao"], df_servidores["Falhas_Ultimos_30_Dias"], c=cores)
plt.xlabel("Dias desde manutencao")
plt.ylabel("Falhas ultimos 30 dias")
plt.title("Manutencao vs Falhas")
plt.tight_layout()
plt.show()

print("\nInterpretacao dos graficos:")
print("As salas de risco alto apresentam, em geral, mais consumo, alertas, falhas e dias desde manutencao.")

X = df_servidores[[
    "Temperatura_C",
    "Humidade_Percentagem",
    "Consumo_kWh",
    "Alertas_24h",
    "Dias_Desde_Manutencao",
    "Falhas_Ultimos_30_Dias",
    "Servidores_Ativos",
]]
y = df_servidores["Nivel_Risco"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

print("\nTamanhos dos conjuntos:")
print(X_train.shape)
print(X_test.shape)

modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
modelo.fit(X_train, y_train)
previsoes = modelo.predict(X_test)

comparacao = pd.DataFrame({
    "Real": y_test.values,
    "Previsto": previsoes,
})

print("\nComparacao:")
print(comparacao)

accuracy = accuracy_score(y_test, previsoes)
matriz = confusion_matrix(y_test, previsoes, labels=["Baixo", "Medio", "Alto"])
relatorio = classification_report(y_test, previsoes, zero_division=0)

print(f"Accuracy: {accuracy:.2f}")
print("\nMatriz de confusao:")
print(matriz)
print("\nRelatorio de classificacao:")
print(relatorio)

nova_sala = pd.DataFrame({
    "Temperatura_C": [34],
    "Humidade_Percentagem": [75],
    "Consumo_kWh": [275],
    "Alertas_24h": [14],
    "Dias_Desde_Manutencao": [88],
    "Falhas_Ultimos_30_Dias": [5],
    "Servidores_Ativos": [51],
})

previsao_nova = modelo.predict(nova_sala)[0]
print(f"Previsao para a nova sala: {previsao_nova}")

print("\nConclusao final:")
print("O aumento de risco esta associado a temperatura, humidade, consumo, alertas, falhas e atraso na manutencao.")
print("A arvore de decisao consegue lidar com tres classes, mas num contexto real nao seria aceitavel falhar casos de risco alto.")
