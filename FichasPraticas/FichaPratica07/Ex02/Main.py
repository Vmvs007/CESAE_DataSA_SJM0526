import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_escape = {
    "Equipa": [
        "E01", "E02", "E03", "E04", "E05",
        "E06", "E07", "E08", "E09", "E10",
        "E11", "E12", "E13", "E14", "E15",
        "E16", "E17", "E18"
    ],
    "Sala": [
        "Laboratório", "Castelo", "Nave Espacial", "Laboratório", "Templo",
        "Castelo", "Nave Espacial", "Templo", "Laboratório", "Castelo",
        "Templo", "Nave Espacial", "Laboratório", "Castelo", "Templo",
        "Nave Espacial", "Laboratório", "Templo"
    ],
    "Numero_Jogadores": [
        4, 5, 3, 6, 4, 2, 5, 6, 3, 4, 5, 6, 2, 3, 4, 5, 6, 3
    ],
    "Tempo_Minutos": [
        54, 61, 58, 45, 67, 70, 52, 49, 63, 66, 59, 47, 72, 69, 64, 50, 44, 71
    ],
    "Pistas_Usadas": [
        3, 5, 4, 2, 6, 7, 3, 2, 5, 6, 4, 2, 8, 7, 5, 3, 1, 7
    ],
    "Enigmas_Resolvidos": [
        8, 7, 9, 10, 7, 6, 10, 11, 7, 7, 8, 11, 6, 6, 8, 10, 12, 6
    ],
    "Concluiu": [
        True, False, True, True, False, False, True, True, False,
        False, True, True, False, False, True, True, True, False
    ]
}

df_escape = pd.DataFrame(dados_escape)

print("DataFrame:")
print(df_escape)

taxa_geral = df_escape["Concluiu"].mean() * 100

print("\nTaxa geral de conclusão:")
print(f"{taxa_geral:.2f}%")

taxa_por_sala = df_escape.groupby("Sala")["Concluiu"].mean() * 100

print("\nTaxa de conclusão por sala:")
print(taxa_por_sala)

plt.figure(figsize=(8, 5))
taxa_por_sala.sort_values(ascending=False).plot(kind="bar")
plt.title("Taxa de conclusão por sala")
plt.xlabel("Sala")
plt.ylabel("Taxa de conclusão (%)")
plt.xticks(rotation=30)
plt.ylim(0, 100)
plt.show()

tempo_medio_sala = df_escape.groupby("Sala")["Tempo_Minutos"].mean().sort_values(ascending=False)

print("\nTempo médio por sala:")
print(tempo_medio_sala)

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df_escape,
    x="Sala",
    y="Tempo_Minutos"
)
plt.title("Distribuição do tempo por sala")
plt.xlabel("Sala")
plt.ylabel("Tempo em minutos")
plt.xticks(rotation=30)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_escape,
    x="Pistas_Usadas",
    y="Tempo_Minutos",
    hue="Sala",
    style="Concluiu"
)
plt.title("Relação entre pistas usadas e tempo de conclusão")
plt.xlabel("Pistas usadas")
plt.ylabel("Tempo em minutos")
plt.show()

correlacao_pistas_tempo = df_escape["Pistas_Usadas"].corr(df_escape["Tempo_Minutos"])
correlacao_jogadores_tempo = df_escape["Numero_Jogadores"].corr(df_escape["Tempo_Minutos"])
correlacao_enigmas_tempo = df_escape["Enigmas_Resolvidos"].corr(df_escape["Tempo_Minutos"])

print("\nCorrelação entre pistas usadas e tempo:")
print(correlacao_pistas_tempo)

print("\nCorrelação entre número de jogadores e tempo:")
print(correlacao_jogadores_tempo)

print("\nCorrelação entre enigmas resolvidos e tempo:")
print(correlacao_enigmas_tempo)

df_escape["Resultado"] = df_escape["Concluiu"].map({
    True: "Escapou",
    False: "Não escapou"
})

print("\nDataFrame com a nova coluna Resultado:")
print(df_escape)

tabela_cruzada = pd.crosstab(df_escape["Sala"], df_escape["Resultado"])

print("\nTabela cruzada entre Sala e Resultado:")
print(tabela_cruzada)

print("\nConclusão:")
print("""
A taxa geral de conclusão é de 55.56%, ou seja, pouco mais de metade das equipas conseguiu escapar.

A sala mais difícil parece ser o Castelo, uma vez que apresenta uma taxa de conclusão de 0%
e o tempo médio mais elevado, com 66.5 minutos.

A sala com melhor desempenho é a Nave Espacial, com uma taxa de conclusão de 100%
e o menor tempo médio, com 51.75 minutos.

Existe uma correlação muito forte e positiva entre o número de pistas usadas e o tempo,
aproximadamente 0.98. Isto indica que as equipas que usaram mais pistas tenderam
também a demorar mais tempo.

A correlação entre número de jogadores e tempo é negativa, aproximadamente -0.87,
o que sugere que equipas maiores tenderam a concluir os jogos mais rapidamente.

A correlação entre enigmas resolvidos e tempo também é negativa, aproximadamente -0.95,
indicando que equipas que resolveram mais enigmas tenderam a demorar menos tempo.

Assim, a empresa pode concluir que o Castelo deve ser revisto, pois parece demasiado difícil,
enquanto a Nave Espacial apresenta o melhor equilíbrio entre sucesso e tempo de conclusão.
""")