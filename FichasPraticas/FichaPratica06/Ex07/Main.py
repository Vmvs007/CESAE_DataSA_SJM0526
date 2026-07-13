from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
ficheiro = pasta / "vendas_irmaos_botins.xlsx"

dados = {
    "Loja": ["Loja Norte", "Loja Norte", "Loja Norte", "Loja Centro", "Loja Centro", "Loja Centro", "Loja Sul", "Loja Sul", "Loja Sul", "Loja Online", "Loja Online", "Loja Online"],
    "Cidade": ["Porto", "Porto", "Porto", "Coimbra", "Coimbra", "Coimbra", "Lisboa", "Lisboa", "Lisboa", "Online", "Online", "Online"],
    "Mes": ["Janeiro", "Fevereiro", "Marco", "Janeiro", "Fevereiro", "Marco", "Janeiro", "Fevereiro", "Marco", "Janeiro", "Fevereiro", "Marco"],
    "Vendas": [12500, 13800, 14200, 9800, 10500, 11100, 15200, 14900, 16000, 18500, 20100, 22300],
}

pd.DataFrame(dados).to_excel(ficheiro, index=False, sheet_name="Vendas")

df = pd.read_excel(ficheiro)

print("Primeiras linhas:")
print(df.head())

vendas_loja_cidade = df.groupby(["Loja", "Cidade"])["Vendas"].sum().sort_values(ascending=False)
vendas_por_loja = df.groupby("Loja")["Vendas"].sum().sort_values(ascending=False)
loja_maior_volume = vendas_por_loja.idxmax()
vendas_por_mes = df.groupby("Mes")["Vendas"].sum().sort_values(ascending=False)
mes_maior_volume = vendas_por_mes.idxmax()

tabela_dinamica = pd.pivot_table(
    df,
    values="Vendas",
    index="Loja",
    columns="Mes",
    aggfunc="sum",
)

media_vendas_loja = df.groupby("Loja")["Vendas"].mean()

def classificar_desempenho(vendas):
    if vendas >= 18000:
        return "Excelente"
    if vendas >= 12000:
        return "Bom"
    return "A melhorar"

df["Desempenho"] = df["Vendas"].apply(classificar_desempenho)

print("\nVendas totais por loja e cidade:")
print(vendas_loja_cidade)
print(f"Loja com maior volume total: {loja_maior_volume}")
print(f"Mes com maior volume total: {mes_maior_volume}")
print("\nTabela dinamica:")
print(tabela_dinamica)
print("\nLojas ordenadas por vendas totais:")
print(vendas_por_loja)
print("\nMedia de vendas por loja:")
print(media_vendas_loja)
print("\nDataFrame com desempenho:")
print(df)

tabela_dinamica.to_excel(pasta / "tabela_dinamica_vendas.xlsx")
print("\nExportado com sucesso: tabela_dinamica_vendas.xlsx")
