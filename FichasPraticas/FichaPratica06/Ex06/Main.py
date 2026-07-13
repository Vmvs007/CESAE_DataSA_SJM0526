from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_json(pasta / "encomendas_online.json")

print("Todas as encomendas:")
print(df)

encomendas_estado = df["Estado"].value_counts()
concluidas = df[df["Estado"].str.contains("Conclu", case=False, na=False)]
valor_total_concluidas = concluidas["Valor"].sum()
valor_categoria = concluidas.groupby("Categoria")["Valor"].sum().sort_values(ascending=False)
categoria_maior_faturacao = valor_categoria.idxmax()
encomendas_ordenadas = df.sort_values("Valor", ascending=False)
df["Valor_Com_IVA"] = df["Valor"] * 1.23

print("\nEncomendas por estado:")
print(encomendas_estado)
print("\nEncomendas concluidas:")
print(concluidas)
print(f"Valor total das encomendas concluidas: {valor_total_concluidas:.2f} EUR")
print("\nValor total por categoria:")
print(valor_categoria)
print(f"Categoria com maior faturacao: {categoria_maior_faturacao}")
print("\nEncomendas ordenadas por valor:")
print(encomendas_ordenadas)
print("\nDataFrame com IVA:")
print(df)

concluidas.to_excel(pasta / "encomendas_concluidas.xlsx", index=False)
valor_categoria.reset_index().to_csv(pasta / "resumo_categoria.csv", sep=";", index=False)
print("\nExportacoes concluidas com sucesso.")
