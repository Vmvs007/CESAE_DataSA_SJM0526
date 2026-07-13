from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
df = pd.read_csv(pasta / "dados_sujos_alunos.csv", sep=";")

print("DataFrame original:")
print(df)

df["Nome"] = df["Nome"].str.strip()

print("\nValores em falta por coluna:")
print(df.isnull().sum())

df = df.drop_duplicates()
df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce")
media_idades_validas = round(df["Idade"].mean())
df["Idade"] = df["Idade"].fillna(media_idades_validas).astype(int)

df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
df["Nota"] = df["Nota"].clip(lower=0, upper=20)
media_notas = df["Nota"].mean()
df["Nota"] = df["Nota"].fillna(media_notas)

df["Estado"] = df["Nota"].apply(lambda nota: "Aprovado" if nota >= 10 else "Reprovado")

print("\nDataFrame limpo:")
print(df)

df.to_csv(pasta / "dados_alunos_limpos.csv", sep=";", index=False)
print("\nExportado com sucesso: dados_alunos_limpos.csv")
