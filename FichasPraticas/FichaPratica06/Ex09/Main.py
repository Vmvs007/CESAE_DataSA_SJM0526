from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
ficheiro = pasta / "controlo_stock.xlsx"

dados = {
    "Produto": ["Caderno A4", "Caneta Azul", "Mochila Escolar", "Calculadora Cientifica", "Marcadores", "Estojo", "Pen USB 64GB", "Agenda 2026", "Regua 30cm", "Auriculares", "Lapis HB", "Compasso"],
    "Categoria": ["Papelaria", "Papelaria", "Acessorios", "Tecnologia", "Papelaria", "Acessorios", "Tecnologia", "Papelaria", "Papelaria", "Tecnologia", "Papelaria", "Papelaria"],
    "Stock": [120, 300, 8, 15, 35, 12, 6, 20, 80, 5, 400, 9],
    "Stock_Minimo": [50, 100, 10, 10, 30, 15, 10, 20, 40, 10, 150, 10],
    "Fornecedor": ["Fornecedor A", "Fornecedor A", "Fornecedor B", "Fornecedor C", "Fornecedor A", "Fornecedor B", "Fornecedor C", "Fornecedor A", "Fornecedor A", "Fornecedor C", "Fornecedor A", "Fornecedor B"],
}

pd.DataFrame(dados).to_excel(ficheiro, index=False, sheet_name="Stock")

df = pd.read_excel(ficheiro)

print("DataFrame completo:")
print(df)

df["Necessita_Reposicao"] = df["Stock"] < df["Stock_Minimo"]
produtos_reposicao = df[df["Necessita_Reposicao"] == True]
produtos_por_fornecedor = df["Fornecedor"].value_counts()
stock_medio_categoria = df.groupby("Categoria")["Stock"].mean().sort_values()
categoria_menor_stock = stock_medio_categoria.idxmin()
produtos_ordenados_stock = df.sort_values("Stock")
df["Diferenca_Stock"] = df["Stock"] - df["Stock_Minimo"]

print("\nProdutos que precisam de reposicao:")
print(produtos_reposicao)
print("\nProdutos por fornecedor:")
print(produtos_por_fornecedor)
print("\nStock medio por categoria:")
print(stock_medio_categoria)
print(f"Categoria com menor stock medio: {categoria_menor_stock}")
print("\nProdutos ordenados por stock:")
print(produtos_ordenados_stock)
print("\nDataFrame com diferenca de stock:")
print(df)

produtos_reposicao.to_excel(pasta / "relatorio_reposicao.xlsx", index=False)
print("\nExportado com sucesso: relatorio_reposicao.xlsx")
