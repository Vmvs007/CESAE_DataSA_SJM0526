import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


dados = {
    "Km_Percorridos": [120, 340, 560, 230, 780, 150, 910, 430, 670, 290, 1020, 510, 860, 190, 720, 390, 1150, 610, 310, 940, 480, 800, 260, 1080, 370, 690, 130, 990, 540, 750],
    "Numero_Viagens": [35, 90, 140, 60, 190, 42, 230, 115, 170, 75, 260, 130, 215, 50, 185, 100, 300, 155, 82, 240, 125, 200, 68, 280, 96, 175, 38, 255, 138, 195],
    "Travagens_Bruscas": [8, 22, 35, 14, 48, 10, 60, 28, 42, 18, 70, 33, 55, 12, 46, 25, 82, 39, 20, 64, 31, 50, 16, 76, 24, 44, 9, 68, 34, 49],
    "Dias_Desde_Manutencao": [12, 35, 58, 20, 75, 15, 90, 42, 63, 28, 100, 50, 82, 18, 70, 38, 115, 60, 30, 95, 46, 78, 25, 108, 36, 66, 14, 98, 52, 72],
    "Utilizacao_Chuva": [2, 7, 12, 4, 16, 3, 20, 8, 14, 5, 22, 10, 18, 3, 15, 7, 25, 13, 6, 21, 9, 17, 4, 24, 7, 14, 2, 23, 11, 16],
    "Desgaste_Percentagem": [9, 24, 39, 16, 55, 11, 68, 31, 47, 20, 76, 36, 62, 14, 52, 28, 88, 43, 22, 70, 34, 58, 18, 82, 27, 49, 10, 74, 38, 54],
}

df_trotinetes = pd.DataFrame(dados)

print("Primeiras 5 linhas:")
print(df_trotinetes.head())
print("\nInfo:")
df_trotinetes.info()
print("\nEstatisticas descritivas:")
print(df_trotinetes.describe())
print("\nValores em falta:")
print(df_trotinetes.isnull().sum())
print("\nResumo do desgaste:")
print(df_trotinetes["Desgaste_Percentagem"].agg(["min", "max", "mean"]))

media_desgaste = df_trotinetes["Desgaste_Percentagem"].mean()
maior_desgaste = df_trotinetes.loc[df_trotinetes["Desgaste_Percentagem"].idxmax()]
menor_desgaste = df_trotinetes.loc[df_trotinetes["Desgaste_Percentagem"].idxmin()]
correlacoes = df_trotinetes.corr(numeric_only=True)
relacao_desgaste = correlacoes["Desgaste_Percentagem"].drop("Desgaste_Percentagem").sort_values(key=abs, ascending=False)

print(f"Media de desgaste: {media_desgaste:.2f}%")
print("\nTrotinete com maior desgaste:")
print(maior_desgaste)
print("\nTrotinete com menor desgaste:")
print(menor_desgaste)
print("\nCorrelacoes:")
print(correlacoes)
print("\nVariaveis mais relacionadas com o desgaste:")
print(relacao_desgaste)

for coluna in ["Km_Percorridos", "Travagens_Bruscas", "Dias_Desde_Manutencao"]:
    plt.figure(figsize=(7, 4))
    plt.scatter(df_trotinetes[coluna], df_trotinetes["Desgaste_Percentagem"])
    plt.xlabel(coluna)
    plt.ylabel("Desgaste (%)")
    plt.title(f"Relacao entre {coluna} e desgaste")
    plt.tight_layout()
    plt.show()

print("\nInterpretacao dos graficos:")
print("Os graficos mostram relacao positiva entre utilizacao, travagens, tempo desde manutencao e desgaste.")

X = df_trotinetes[[
    "Km_Percorridos",
    "Numero_Viagens",
    "Travagens_Bruscas",
    "Dias_Desde_Manutencao",
    "Utilizacao_Chuva",
]]
y = df_trotinetes["Desgaste_Percentagem"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("\nTamanhos dos conjuntos:")
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

coeficientes = pd.DataFrame({
    "Variavel": X.columns,
    "Coeficiente": modelo.coef_,
})

print("\nCoeficientes:")
print(coeficientes)
print(f"Intercepto: {modelo.intercept_:.2f}")

previsoes = modelo.predict(X_test)
resultado = pd.DataFrame({
    "Valor_Real": y_test.values,
    "Valor_Previsto": previsoes,
})
resultado["Erro_Absoluto"] = abs(resultado["Valor_Real"] - resultado["Valor_Previsto"])

print("\nComparacao entre valores reais e previstos:")
print(resultado.sort_values("Erro_Absoluto", ascending=False))

mae = mean_absolute_error(y_test, previsoes)
r2 = r2_score(y_test, previsoes)

print(f"MAE: {mae:.2f}")
print(f"R2: {r2:.2f}")

nova_trotinete = pd.DataFrame({
    "Km_Percorridos": [850],
    "Numero_Viagens": [210],
    "Travagens_Bruscas": [52],
    "Dias_Desde_Manutencao": [80],
    "Utilizacao_Chuva": [18],
})

desgaste_previsto = modelo.predict(nova_trotinete)
print(f"Desgaste previsto para a nova trotinete: {desgaste_previsto[0]:.2f}%")

print("\nConclusao final:")
print("As variaveis de utilizacao acumulada apresentam forte relacao com o desgaste.")
print("Com MAE baixo e R2 elevado, a regressao linear consegue apoiar manutencao preventiva.")
print("Antes de usar em ambiente real, seria necessario validar o modelo com mais dados.")
