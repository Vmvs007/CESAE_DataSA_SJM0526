import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


dados = {
    "Temperatura_C": [22, 24, 29, 31, 21, 26, 33, 23, 28, 35, 20, 25, 30, 34, 22, 27, 32, 24, 29, 36, 21, 26, 31, 33, 23, 28, 35, 20, 25, 30],
    "Humidade_Percentagem": [68, 65, 50, 42, 72, 60, 38, 70, 55, 35, 75, 63, 48, 40, 69, 58, 43, 66, 52, 33, 73, 61, 45, 39, 71, 54, 36, 76, 62, 49],
    "CO2_ppm": [420, 460, 700, 850, 400, 520, 920, 430, 680, 980, 390, 500, 780, 900, 440, 610, 870, 470, 720, 1020, 410, 530, 810, 890, 450, 690, 960, 395, 510, 760],
    "Horas_Luz": [8, 9, 11, 13, 8, 10, 14, 9, 12, 15, 7, 10, 13, 14, 8, 11, 13, 9, 12, 15, 7, 10, 13, 14, 8, 12, 15, 7, 10, 13],
    "Agua_Litros_Dia": [35, 38, 50, 58, 32, 42, 65, 36, 48, 70, 30, 40, 55, 62, 34, 45, 60, 37, 51, 74, 31, 43, 57, 64, 35, 49, 72, 29, 41, 54],
    "Dias_Desde_Inspecao": [3, 6, 14, 20, 2, 9, 25, 4, 13, 30, 1, 8, 18, 24, 5, 11, 22, 7, 16, 32, 2, 10, 19, 26, 4, 15, 29, 1, 9, 17],
    "Pragas_Detetadas": [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    "Intervencao_Urgente": ["Nao", "Nao", "Sim", "Sim", "Nao", "Nao", "Sim", "Nao", "Sim", "Sim", "Nao", "Nao", "Sim", "Sim", "Nao", "Nao", "Sim", "Nao", "Sim", "Sim", "Nao", "Nao", "Sim", "Sim", "Nao", "Sim", "Sim", "Nao", "Nao", "Sim"],
}

df_estufas = pd.DataFrame(dados)

print("Primeiras linhas:")
print(df_estufas.head())
print("\nInfo:")
df_estufas.info()
print("\nEstatisticas descritivas:")
print(df_estufas.describe())
print("\nValores em falta:")
print(df_estufas.isnull().sum())
print("\nClasses:")
print(df_estufas["Intervencao_Urgente"].value_counts())

print("\nMedia da temperatura por intervencao:")
print(df_estufas.groupby("Intervencao_Urgente")["Temperatura_C"].mean())
print("\nMedia da humidade por intervencao:")
print(df_estufas.groupby("Intervencao_Urgente")["Humidade_Percentagem"].mean())
print("\nMedia de CO2 por intervencao:")
print(df_estufas.groupby("Intervencao_Urgente")["CO2_ppm"].mean())
print("\nTabela cruzada entre pragas e intervencao:")
print(pd.crosstab(df_estufas["Pragas_Detetadas"], df_estufas["Intervencao_Urgente"]))

df_estufas["Intervencao_Urgente"].value_counts().plot(kind="bar")
plt.title("Contagem de estufas por classe")
plt.xlabel("Intervencao urgente")
plt.ylabel("Numero de estufas")
plt.tight_layout()
plt.show()

cores = df_estufas["Intervencao_Urgente"].map({"Nao": "green", "Sim": "red"})
plt.figure(figsize=(7, 4))
plt.scatter(df_estufas["Temperatura_C"], df_estufas["Humidade_Percentagem"], c=cores)
plt.xlabel("Temperatura")
plt.ylabel("Humidade")
plt.title("Temperatura vs Humidade por classe")
plt.tight_layout()
plt.show()

df_estufas.groupby("Intervencao_Urgente")["CO2_ppm"].mean().plot(kind="bar")
plt.title("Media de CO2 por classe")
plt.xlabel("Intervencao urgente")
plt.ylabel("CO2 ppm")
plt.tight_layout()
plt.show()

print("\nInterpretacao dos graficos:")
print("As estufas urgentes concentram temperaturas, CO2, agua e dias desde inspecao mais elevados.")

X = df_estufas[[
    "Temperatura_C",
    "Humidade_Percentagem",
    "CO2_ppm",
    "Horas_Luz",
    "Agua_Litros_Dia",
    "Dias_Desde_Inspecao",
    "Pragas_Detetadas",
]]
y = df_estufas["Intervencao_Urgente"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

print("\nTamanhos dos conjuntos:")
print(X_train.shape)
print(X_test.shape)

modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
comparacao = pd.DataFrame({
    "Real": y_test.values,
    "Previsto": previsoes,
})

print("\nComparacao:")
print(comparacao)

accuracy = accuracy_score(y_test, previsoes)
matriz = confusion_matrix(y_test, previsoes, labels=["Nao", "Sim"])
relatorio = classification_report(y_test, previsoes, zero_division=0)

print(f"Accuracy: {accuracy:.2f}")
print("\nMatriz de confusao:")
print(matriz)
print("\nRelatorio de classificacao:")
print(relatorio)

nova_estufa = pd.DataFrame({
    "Temperatura_C": [34],
    "Humidade_Percentagem": [41],
    "CO2_ppm": [910],
    "Horas_Luz": [14],
    "Agua_Litros_Dia": [66],
    "Dias_Desde_Inspecao": [27],
    "Pragas_Detetadas": [1],
})

previsao_nova = modelo.predict(nova_estufa)[0]
print(f"Previsao para a nova estufa: {previsao_nova}")

print("\nConclusao final:")
print("Temperatura alta, humidade baixa, CO2 elevado, mais dias desde inspecao e pragas aparecem associados a intervencao urgente.")
print("A arvore de decisao e adequada para explicar regras simples, mas deve ser validada com mais dados antes de uso real.")
