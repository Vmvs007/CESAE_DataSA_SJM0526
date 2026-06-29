import pandas as pd

df = pd.read_csv("vendas_loja.csv", sep=";", decimal=",")

print("Primeiras 5 linhas: ")
print(df.head())

print("\nInfo:")
print(df.info())

df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])

df["Total_Venda"] = df["Preco"] * df["Quantidade"]

# Vendas superiores a 50€
vendas_superiores_50 = df[df["Total_Venda"] > 50]

print("\nVendas Superiores a 50€: ")
print(vendas_superiores_50)

# Agrupar por Categoria
total_categoria = df.groupby("Categoria")["Total_Venda"].sum()

'''
total_categoria = df.groupby("Categoria").agg({
    "Quantidade":"sum",
    "Total_Venda":"sum"
})
'''

print("\nTotal Vendido por Categoria: ")
print(total_categoria)

# Ordenar produtos mais vendidos
print("\nProdutos mais vendidos:")
produtos_best_sellers = df.groupby("Produto")["Quantidade"].sum()
produtos_best_sellers = produtos_best_sellers.sort_values(ascending=False)

print(produtos_best_sellers)

# Exportar
df.to_csv("vendas_loja_tratado.csv", sep=";", index=False)
print("Exportado com sucesso")
