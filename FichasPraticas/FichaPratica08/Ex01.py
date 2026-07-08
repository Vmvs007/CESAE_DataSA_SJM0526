import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_ruido = {
    "Zona": [
        "Centro", "Centro", "Centro", "Centro",
        "Parque", "Parque", "Parque", "Parque",
        "Industrial", "Industrial", "Industrial", "Industrial",
        "Residencial", "Residencial", "Residencial", "Residencial",
        "Ribeira", "Ribeira", "Ribeira", "Ribeira"
    ],
    "Periodo": [
        "Manhã", "Tarde", "Noite", "Madrugada",
        "Manhã", "Tarde", "Noite", "Madrugada",
        "Manhã", "Tarde", "Noite", "Madrugada",
        "Manhã", "Tarde", "Noite", "Madrugada",
        "Manhã", "Tarde", "Noite", "Madrugada"
    ],
    "Dia_Tipo": [
        "Útil", "Útil", "Útil", "Fim de semana",
        "Útil", "Útil", "Fim de semana", "Fim de semana",
        "Útil", "Útil", "Útil", "Fim de semana",
        "Útil", "Útil", "Fim de semana", "Fim de semana",
        "Útil", "Útil", "Fim de semana", "Fim de semana"
    ],
    "Nivel_Ruido_dB": [
        68, 72, 76, 61,
        48, 52, 55, 43,
        74, 79, 70, 58,
        55, 59, 62, 47,
        63, 69, 81, 66
    ],
    "Numero_Pessoas": [
        320, 450, 520, 120,
        80, 130, 160, 30,
        210, 260, 170, 60,
        150, 190, 220, 50,
        280, 390, 610, 230
    ],
    "Temperatura": [
        18, 23, 20, 15,
        17, 22, 19, 14,
        19, 25, 21, 16,
        18, 24, 20, 15,
        18, 23, 21, 16
    ]
}

df_ruido = pd.DataFrame(dados_ruido)

print("Primeiras linhas do DataFrame:")
print(df_ruido.head())

print("\nEstatísticas descritivas:")
print(df_ruido.describe())

media_zona = df_ruido.groupby("Zona")["Nivel_Ruido_dB"].mean().sort_values(ascending=False)

print("\nNível médio de ruído por zona:")
print(media_zona)

plt.figure(figsize=(8, 5))
media_zona.plot(kind="barh")
plt.title("Nível médio de ruído por zona")
plt.xlabel("Nível médio de ruído (dB)")
plt.ylabel("Zona")
plt.gca().invert_yaxis()
plt.show()

media_periodo = df_ruido.groupby("Periodo")["Nivel_Ruido_dB"].mean().sort_values(ascending=False)

print("\nNível médio de ruído por período:")
print(media_periodo)

plt.figure(figsize=(8, 5))
media_periodo.plot(kind="bar")
plt.title("Nível médio de ruído por período do dia")
plt.xlabel("Período")
plt.ylabel("Nível médio de ruído (dB)")
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_ruido,
    x="Numero_Pessoas",
    y="Nivel_Ruido_dB",
    hue="Zona"
)
plt.title("Relação entre número de pessoas e nível de ruído")
plt.xlabel("Número de pessoas")
plt.ylabel("Nível de ruído (dB)")
plt.show()

correlacao = df_ruido["Numero_Pessoas"].corr(df_ruido["Nivel_Ruido_dB"])

print("\nCorrelação entre número de pessoas e nível de ruído:")
print(correlacao)

tabela_dinamica = pd.pivot_table(
    df_ruido,
    values="Nivel_Ruido_dB",
    index="Zona",
    columns="Periodo",
    aggfunc="mean"
)

print("\nTabela dinâmica - média de ruído por zona e período:")
print(tabela_dinamica)

print("\nConclusão:")
print("""
A zona mais ruidosa é a zona Industrial, com uma média de 70.25 dB,
seguida da Ribeira e do Centro.

O período mais crítico é a Noite, com uma média de 68.8 dB,
sendo o período com maior exposição sonora média.

A correlação entre o número de pessoas e o nível de ruído é aproximadamente 0.81,
o que indica uma relação positiva forte. Isto significa que, em geral,
quanto maior é a concentração de pessoas, maior tende a ser o nível de ruído.

Como recomendação, a autarquia poderia reforçar a monitorização nas zonas Industrial,
Ribeira e Centro, especialmente durante a noite, aplicando medidas como controlo
de tráfego, limitação de atividades ruidosas em determinados horários e criação
de zonas de redução sonora.
""")