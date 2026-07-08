from tokenize import group

import pandas as pd
import matplotlib.pyplot as plt

###################################################
#               1. Carregar Dataset               #
###################################################

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

print(df_ruido.head())

print(df_ruido.info())

###################################################
#               2. Primeira Análise               #
###################################################

print("\n_________________________________________________\n")
group_media_ruido_zona = df_ruido.groupby("Zona")["Nivel_Ruido_dB"].mean().sort_values()
print(group_media_ruido_zona)

group_media_ruido_zona.plot(kind="barh")
plt.show()

print("\n_________________________________________________\n")

group_media_ruido_dia = df_ruido.groupby("Dia_Tipo")["Nivel_Ruido_dB"].mean().sort_values()
print(group_media_ruido_dia)

group_media_ruido_dia.plot(kind="bar")
plt.show()

print("\n_________________________________________________\n")


