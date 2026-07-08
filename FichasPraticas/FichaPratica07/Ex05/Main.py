import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_biblioteca = {
    "Espaco": [
        "Leitura Silenciosa", "Leitura Silenciosa", "Leitura Silenciosa",
        "Makerspace", "Makerspace", "Makerspace",
        "Sala Multimédia", "Sala Multimédia", "Sala Multimédia",
        "Arquivo Histórico", "Arquivo Histórico", "Arquivo Histórico",
        "Zona Infantil", "Zona Infantil", "Zona Infantil"
    ],
    "Periodo": [
        "Manhã", "Tarde", "Noite",
        "Manhã", "Tarde", "Noite",
        "Manhã", "Tarde", "Noite",
        "Manhã", "Tarde", "Noite",
        "Manhã", "Tarde", "Noite"
    ],
    "Visitantes": [
        45, 62, 38,
        18, 41, 27,
        25, 55, 49,
        12, 20, 9,
        35, 58, 22
    ],
    "Tempo_Medio_Min": [
        95, 110, 85,
        70, 120, 100,
        60, 90, 80,
        130, 150, 100,
        45, 55, 40
    ],
    "Reservas": [
        20, 34, 18,
        10, 29, 21,
        15, 38, 33,
        6, 11, 4,
        8, 14, 5
    ],
    "Eventos_Decorridos": [
        0, 1, 0,
        1, 3, 2,
        1, 2, 2,
        0, 1, 0,
        2, 3, 1
    ]
}

df_biblioteca = pd.DataFrame(dados_biblioteca)

print("DataFrame:")
print(df_biblioteca)

total_visitantes = df_biblioteca["Visitantes"].sum()

print("\nNúmero total de visitantes:")
print(total_visitantes)

visitantes_por_espaco = df_biblioteca.groupby("Espaco")["Visitantes"].sum().sort_values(ascending=False)

print("\nTotal de visitantes por espaço:")
print(visitantes_por_espaco)

plt.figure(figsize=(8, 5))
visitantes_por_espaco.plot(kind="barh")
plt.title("Total de visitantes por espaço")
plt.xlabel("Número de visitantes")
plt.ylabel("Espaço")
plt.gca().invert_yaxis()
plt.show()

tempo_medio_espaco = df_biblioteca.groupby("Espaco")["Tempo_Medio_Min"].mean().sort_values(ascending=False)

print("\nTempo médio de permanência por espaço:")
print(tempo_medio_espaco)

plt.figure(figsize=(8, 5))
tempo_medio_espaco.plot(kind="bar")
plt.title("Tempo médio de permanência por espaço")
plt.xlabel("Espaço")
plt.ylabel("Tempo médio em minutos")
plt.xticks(rotation=30, ha="right")
plt.show()

visitantes_por_periodo = df_biblioteca.groupby("Periodo")["Visitantes"].sum().sort_values(ascending=False)

print("\nNúmero total de visitantes por período:")
print(visitantes_por_periodo)

tabela_dinamica = pd.pivot_table(
    df_biblioteca,
    values="Visitantes",
    index="Espaco",
    columns="Periodo",
    aggfunc="sum"
)

print("\nTabela dinâmica - visitantes por espaço e período:")
print(tabela_dinamica)

tabela_dinamica.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Visitantes por espaço e período")
plt.xlabel("Espaço")
plt.ylabel("Número de visitantes")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Período")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_biblioteca,
    x="Reservas",
    y="Visitantes",
    hue="Espaco"
)
plt.title("Relação entre reservas e visitantes")
plt.xlabel("Número de reservas")
plt.ylabel("Número de visitantes")
plt.show()

correlacao_reservas_visitantes = df_biblioteca["Reservas"].corr(df_biblioteca["Visitantes"])

print("\nCorrelação entre reservas e visitantes:")
print(correlacao_reservas_visitantes)

print("\nConclusão:")
print("""
O número total de visitantes registado foi de 516.

O espaço mais procurado foi a Leitura Silenciosa, com 145 visitantes,
seguido da Sala Multimédia, com 129 visitantes, e da Zona Infantil, com 115 visitantes.

O período de maior utilização foi a Tarde, com 236 visitantes,
mostrando que este é o momento do dia com maior procura pelos espaços da biblioteca.

O espaço onde os utilizadores permanecem mais tempo é o Arquivo Histórico,
com uma média de aproximadamente 126.67 minutos. Isto pode indicar uma utilização
mais demorada e focada, associada a pesquisa ou consulta de documentos.

A correlação entre reservas e visitantes é aproximadamente 0.91,
o que indica uma relação positiva muito forte. Ou seja, quando o número de reservas aumenta,
o número de visitantes também tende a aumentar.

Como recomendação, a biblioteca pode reforçar os recursos humanos e logísticos durante
o período da tarde, especialmente nos espaços de Leitura Silenciosa, Sala Multimédia
e Zona Infantil. Também poderá ser útil melhorar o sistema de reservas, uma vez que
este parece estar fortemente relacionado com a afluência aos espaços.
""")