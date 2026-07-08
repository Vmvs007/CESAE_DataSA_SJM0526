import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_drones = {
    "Drone": [
        "D01", "D02", "D03", "D04", "D05", "D06",
        "D07", "D08", "D09", "D10", "D11", "D12",
        "D13", "D14", "D15", "D16", "D17", "D18"
    ],
    "Rota": [
        "A-B", "A-C", "B-D", "C-D", "A-D", "B-C",
        "A-B", "A-C", "B-D", "C-D", "A-D", "B-C",
        "A-B", "A-C", "B-D", "C-D", "A-D", "B-C"
    ],
    "Distancia_Km": [
        1.2, 2.8, 3.1, 2.4, 4.5, 1.8,
        1.3, 2.9, 3.4, 2.2, 4.7, 1.6,
        1.1, 3.0, 3.2, 2.5, 4.9, 1.7
    ],
    "Vento_Kmh": [
        8, 12, 20, 15, 28, 10,
        6, 18, 24, 14, 31, 9,
        7, 21, 23, 16, 34, 11
    ],
    "Bateria_Consumida": [
        18, 35, 48, 37, 69, 24,
        17, 42, 53, 36, 75, 23,
        16, 46, 51, 39, 80, 25
    ],
    "Tempo_Minutos": [
        7, 15, 18, 13, 27, 10,
        6, 16, 20, 12, 29, 9,
        6, 17, 19, 14, 31, 10
    ],
    "Entrega_Sucesso": [
        True, True, True, True, False, True,
        True, True, False, True, False, True,
        True, True, True, True, False, True
    ]
}

df_drones = pd.DataFrame(dados_drones)

print("DataFrame:")
print(df_drones)

taxa_sucesso_geral = df_drones["Entrega_Sucesso"].mean() * 100

print("\nTaxa geral de sucesso das entregas:")
print(f"{taxa_sucesso_geral:.2f}%")

taxa_sucesso_rota = df_drones.groupby("Rota")["Entrega_Sucesso"].mean() * 100

print("\nTaxa de sucesso por rota:")
print(taxa_sucesso_rota)

plt.figure(figsize=(8, 5))
taxa_sucesso_rota.sort_values(ascending=False).plot(kind="bar")
plt.title("Taxa de sucesso por rota")
plt.xlabel("Rota")
plt.ylabel("Taxa de sucesso (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.show()

consumo_medio_rota = df_drones.groupby("Rota")["Bateria_Consumida"].mean().sort_values(ascending=False)

print("\nConsumo médio de bateria por rota:")
print(consumo_medio_rota)

plt.figure(figsize=(8, 5))
consumo_medio_rota.plot(kind="barh")
plt.title("Consumo médio de bateria por rota")
plt.xlabel("Bateria consumida")
plt.ylabel("Rota")
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_drones,
    x="Distancia_Km",
    y="Bateria_Consumida",
    hue="Rota"
)
plt.title("Relação entre distância e bateria consumida")
plt.xlabel("Distância em km")
plt.ylabel("Bateria consumida")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_drones,
    x="Vento_Kmh",
    y="Bateria_Consumida",
    hue="Rota"
)
plt.title("Relação entre vento e bateria consumida")
plt.xlabel("Vento em km/h")
plt.ylabel("Bateria consumida")
plt.show()

correlacao_distancia_bateria = df_drones["Distancia_Km"].corr(df_drones["Bateria_Consumida"])
correlacao_vento_bateria = df_drones["Vento_Kmh"].corr(df_drones["Bateria_Consumida"])
correlacao_distancia_tempo = df_drones["Distancia_Km"].corr(df_drones["Tempo_Minutos"])
correlacao_vento_tempo = df_drones["Vento_Kmh"].corr(df_drones["Tempo_Minutos"])

print("\nCorrelação entre distância e bateria:")
print(correlacao_distancia_bateria)

print("\nCorrelação entre vento e bateria:")
print(correlacao_vento_bateria)

print("\nCorrelação entre distância e tempo:")
print(correlacao_distancia_tempo)

print("\nCorrelação entre vento e tempo:")
print(correlacao_vento_tempo)

def classificar_risco(bateria):
    if bateria >= 70:
        return "Alto"
    elif bateria >= 40:
        return "Médio"
    else:
        return "Baixo"

df_drones["Nivel_Risco"] = df_drones["Bateria_Consumida"].apply(classificar_risco)

print("\nDataFrame com a nova coluna Nivel_Risco:")
print(df_drones)

tabela_risco_rota = pd.crosstab(df_drones["Rota"], df_drones["Nivel_Risco"])

print("\nTabela de risco por rota:")
print(tabela_risco_rota)

print("\nConclusão:")
print("""
A taxa geral de sucesso das entregas é de 77.78%, o que indica que a maioria
das entregas experimentais foi concluída com sucesso.

As rotas com melhor taxa de sucesso são A-B, A-C, B-C e C-D, todas com 100%.
A rota A-D é a mais problemática, com 0% de sucesso.

A rota mais exigente é a A-D, pois apresenta o maior consumo médio de bateria,
com aproximadamente 74.67, além de ter a maior distância média e os maiores tempos médios.

Existe uma correlação muito forte entre distância e bateria consumida,
aproximadamente 0.99. Isto indica que, quanto maior é a distância da rota,
maior tende a ser o consumo de bateria.

Também existe uma correlação muito forte entre vento e bateria consumida,
aproximadamente 0.99, sugerindo que o vento pode ter impacto significativo
no consumo energético dos drones.

As rotas com maior risco operacional são sobretudo a A-D, que apresenta casos
de risco Alto, e a B-D, que apresenta vários casos de risco Médio.

Como recomendação, a empresa deve rever a rota A-D, testar limites de autonomia
em condições de vento elevado e definir critérios mínimos de bateria antes de iniciar
rotas mais longas ou mais expostas.
""")