from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_csv(pasta / "presencas_colaboradores.csv", sep=";")

df["Data"] = pd.to_datetime(df["Data"])
df["Entrada_Completa"] = pd.to_datetime(df["Data"].dt.strftime("%Y-%m-%d") + " " + df["Hora_Entrada"])
df["Saida_Completa"] = pd.to_datetime(df["Data"].dt.strftime("%Y-%m-%d") + " " + df["Hora_Saida"])
df["Horas_Trabalhadas"] = (df["Saida_Completa"] - df["Entrada_Completa"]).dt.total_seconds() / 3600

menos_7_horas = df[df["Horas_Trabalhadas"] < 7]
media_departamento = df.groupby("Departamento")["Horas_Trabalhadas"].mean().sort_values(ascending=False)
departamento_maior_media = media_departamento.idxmax()
df["Mes"] = df["Data"].dt.month
resumo_departamento = media_departamento.reset_index()

print(df)
print("\nColaboradores com menos de 7 horas:")
print(menos_7_horas)
print("\nMedia de horas por departamento:")
print(media_departamento)
print(f"Departamento com maior media: {departamento_maior_media}")

resumo_departamento.to_csv(pasta / "resumo_departamento.csv", sep=";", index=False)
print("\nExportado com sucesso: resumo_departamento.csv")
