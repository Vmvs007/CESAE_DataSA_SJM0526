from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_json(pasta / "clientes.json")

print("Estrutura:")
df.info()

total_clientes = len(df)
clientes_ativos = df[df["Cliente_Ativo"] == True]
clientes_por_cidade = df["Cidade"].value_counts()

df["Faixa_Etaria"] = pd.cut(
    df["Idade"],
    bins=[0, 25, 40, 60, 100],
    labels=["Jovem", "Adulto", "Maduro", "Senior"],
    include_lowest=True,
)

clientes_por_faixa = df["Faixa_Etaria"].value_counts().sort_index()
ativos_porto = clientes_ativos[clientes_ativos["Cidade"] == "Porto"]
ordenados_idade = df.sort_values("Idade", ascending=False)

print(f"Total de clientes: {total_clientes}")
print("\nClientes ativos:")
print(clientes_ativos)
print("\nClientes por cidade:")
print(clientes_por_cidade)
print("\nClientes por faixa etaria:")
print(clientes_por_faixa)
print("\nClientes ativos do Porto:")
print(ativos_porto)
print("\nClientes ordenados por idade:")
print(ordenados_idade)

clientes_ativos.to_csv(pasta / "clientes_ativos.csv", sep=";", index=False)
print("\nExportado com sucesso: clientes_ativos.csv")
