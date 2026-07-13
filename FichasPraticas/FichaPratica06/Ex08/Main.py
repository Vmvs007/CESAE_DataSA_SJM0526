from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_csv(pasta / "avaliacoes_clientes.csv", sep=";")

df["Data"] = pd.to_datetime(df["Data"])

avaliacao_media_produto = df.groupby("Produto")["Avaliacao"].mean().sort_values()
numero_avaliacoes_produto = df.groupby("Produto")["Avaliacao"].count().sort_values(ascending=False)
comentarios_negativos = df[df["Avaliacao"] < 3]
produto_pior_avaliacao = avaliacao_media_produto.idxmin()
produto_melhor_avaliacao = avaliacao_media_produto.idxmax()

def classificar_avaliacao(avaliacao):
    if avaliacao >= 4:
        return "Positiva"
    if avaliacao == 3:
        return "Neutra"
    return "Negativa"

df["Classificacao"] = df["Avaliacao"].apply(classificar_avaliacao)
avaliacoes_por_classificacao = df["Classificacao"].value_counts()

print("\nAvaliacao media por produto:")
print(avaliacao_media_produto)
print("\nNumero de avaliacoes por produto:")
print(numero_avaliacoes_produto)
print("\nAvaliacoes inferiores a 3:")
print(comentarios_negativos)
print(f"Produto com pior avaliacao media: {produto_pior_avaliacao}")
print(f"Produto com melhor avaliacao media: {produto_melhor_avaliacao}")
print("\nAvaliacoes por classificacao:")
print(avaliacoes_por_classificacao)

comentarios_negativos.to_csv(pasta / "comentarios_negativos.csv", sep=";", index=False)
print("\nExportado com sucesso: comentarios_negativos.csv")
