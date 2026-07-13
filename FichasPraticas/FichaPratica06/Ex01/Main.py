from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_csv(pasta / "vendas_loja.csv", sep=";", decimal=",")

print("Primeiras 5 linhas:")
print(df.head())

print("\nInfo:")
df.info()

df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])
df["Total_Venda"] = df["Preco"] * df["Quantidade"]

vendas_superiores_50 = df[df["Total_Venda"] > 50]
total_categoria = df.groupby("Categoria")["Total_Venda"].sum().sort_values(ascending=False)
produtos_mais_vendidos = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

print("\nVendas superiores a 50 EUR:")
print(vendas_superiores_50)

print("\nTotal vendido por categoria:")
print(total_categoria)

print("\nProdutos mais vendidos:")
print(produtos_mais_vendidos)

df.to_csv(pasta / "vendas_loja_tratado.csv", sep=";", index=False)
print("\nExportado com sucesso: vendas_loja_tratado.csv")
