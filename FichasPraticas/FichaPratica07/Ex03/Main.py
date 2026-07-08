import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_praias = {
    "Praia": [
        "Praia Norte", "Praia Norte", "Praia Norte", "Praia Norte",
        "Praia Azul", "Praia Azul", "Praia Azul", "Praia Azul",
        "Praia das Rochas", "Praia das Rochas", "Praia das Rochas", "Praia das Rochas",
        "Praia Verde", "Praia Verde", "Praia Verde", "Praia Verde"
    ],
    "Mes": [
        "Março", "Abril", "Maio", "Junho",
        "Março", "Abril", "Maio", "Junho",
        "Março", "Abril", "Maio", "Junho",
        "Março", "Abril", "Maio", "Junho"
    ],
    "Tipo_Residuo": [
        "Plástico", "Vidro", "Plástico", "Beatas",
        "Plástico", "Metal", "Beatas", "Plástico",
        "Vidro", "Plástico", "Metal", "Beatas",
        "Beatas", "Plástico", "Vidro", "Metal"
    ],
    "Peso_Kg": [
        42, 18, 55, 31,
        36, 14, 27, 49,
        22, 60, 19, 34,
        25, 44, 16, 21
    ],
    "Numero_Voluntarios": [
        12, 8, 15, 10,
        11, 7, 9, 14,
        6, 16, 8, 10,
        7, 13, 6, 9
    ],
    "Horas_Recolha": [
        3, 2, 4, 3,
        3, 2, 3, 4,
        2, 4, 2, 3,
        2, 4, 2, 3
    ]
}

df_praias = pd.DataFrame(dados_praias)

print("DataFrame:")
print(df_praias)

peso_total = df_praias["Peso_Kg"].sum()

print("\nPeso total de resíduos recolhidos:")
print(f"{peso_total} kg")

peso_por_praia = df_praias.groupby("Praia")["Peso_Kg"].sum().sort_values(ascending=False)

print("\nPeso total recolhido por praia:")
print(peso_por_praia)

plt.figure(figsize=(8, 5))
peso_por_praia.plot(kind="barh")
plt.title("Peso total de resíduos recolhidos por praia")
plt.xlabel("Peso recolhido (kg)")
plt.ylabel("Praia")
plt.gca().invert_yaxis()
plt.show()

peso_por_residuo = df_praias.groupby("Tipo_Residuo")["Peso_Kg"].sum().sort_values(ascending=False)

print("\nPeso total por tipo de resíduo:")
print(peso_por_residuo)

plt.figure(figsize=(8, 5))
peso_por_residuo.plot(kind="bar")
plt.title("Peso total por tipo de resíduo")
plt.xlabel("Tipo de resíduo")
plt.ylabel("Peso recolhido (kg)")
plt.xticks(rotation=0)
plt.show()

df_praias["Kg_por_Voluntario"] = df_praias["Peso_Kg"] / df_praias["Numero_Voluntarios"]

print("\nPeso médio recolhido por voluntário:")
print(df_praias[["Praia", "Mes", "Peso_Kg", "Numero_Voluntarios", "Kg_por_Voluntario"]])

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_praias,
    x="Numero_Voluntarios",
    y="Peso_Kg",
    hue="Praia"
)
plt.title("Relação entre número de voluntários e peso recolhido")
plt.xlabel("Número de voluntários")
plt.ylabel("Peso recolhido (kg)")
plt.show()

correlacao = df_praias["Numero_Voluntarios"].corr(df_praias["Peso_Kg"])

print("\nCorrelação entre número de voluntários e peso recolhido:")
print(correlacao)

tabela_dinamica = pd.pivot_table(
    df_praias,
    values="Peso_Kg",
    index="Praia",
    columns="Mes",
    aggfunc="sum"
)

print("\nTabela dinâmica - peso recolhido por praia e mês:")
print(tabela_dinamica)

peso_por_mes = df_praias.groupby("Mes")["Peso_Kg"].sum().sort_values(ascending=False)

print("\nPeso total recolhido por mês:")
print(peso_por_mes)

print("\nConclusão:")
print("""
No total, foram recolhidos 513 kg de resíduos nas várias praias analisadas.

A praia com maior volume de resíduos recolhidos foi a Praia Norte, com 146 kg,
seguida da Praia das Rochas, com 135 kg.

O tipo de resíduo mais comum foi o Plástico, com 286 kg recolhidos,
representando claramente a categoria com maior peso no total de resíduos.

O mês com maior recolha foi Abril, com 136 kg, seguido de Junho, com 135 kg.

A correlação entre o número de voluntários e o peso recolhido é aproximadamente 0.96,
o que indica uma relação positiva muito forte. Isto significa que, quanto maior foi
o número de voluntários envolvidos, maior tendeu a ser a quantidade de resíduos recolhida.

Como recomendação, a associação ambiental deve reforçar as ações de sensibilização
relacionadas com o plástico e organizar mais campanhas na Praia Norte e na Praia das Rochas,
envolvendo um maior número de voluntários.
""")