from pathlib import Path
import pandas as pd


pasta = Path(__file__).parent
ficheiro = pasta / "alunos_notas.xlsx"

dados = {
    "Aluno": ["Ana Silva", "Bruno Costa", "Carla Mendes", "Diogo Santos", "Eva Martins", "Fabio Rocha", "Gabriela Pinto", "Hugo Lima", "Ines Ferreira", "Joao Almeida", "Lara Gomes", "Miguel Sousa"],
    "Curso": ["Python", "Java", "Python", "Excel", "Python", "Java", "Excel", "Python", "Java", "Excel", "Python", "Java"],
    "Nota": [17.5, 9.0, 15.5, 11.0, 18.0, 7.5, 13.0, 10.5, 16.0, 8.5, 14.5, 12.0],
    "Faltas": [1, 6, 2, 4, 0, 8, 3, 5, 2, 7, 1, 4],
    "Horas_Estudo": [20, 5, 15, 10, 22, 3, 12, 9, 18, 6, 16, 11],
}

pd.DataFrame(dados).to_excel(ficheiro, index=False, sheet_name="Notas")

df = pd.read_excel(ficheiro)

print("Primeiras linhas:")
print(df.head())
print(f"Linhas e colunas: {df.shape}")

df["Estado"] = df["Nota"].apply(lambda nota: "Aprovado" if nota >= 10 else "Reprovado")

reprovados = df[df["Estado"] == "Reprovado"]
alunos_mais_5_faltas = df[df["Faltas"] > 5]
media_notas_curso = df.groupby("Curso")["Nota"].mean()
media_horas_curso = df.groupby("Curso")["Horas_Estudo"].mean()
melhor_aluno = df.loc[df["Nota"].idxmax()]
aprovados = df[df["Estado"] == "Aprovado"]

print("\nAlunos reprovados:")
print(reprovados)
print("\nAlunos com mais de 5 faltas:")
print(alunos_mais_5_faltas)
print("\nMedia das notas por curso:")
print(media_notas_curso)
print("\nMedia das horas de estudo por curso:")
print(media_horas_curso)
print("\nAluno com melhor nota:")
print(melhor_aluno)

aprovados.to_excel(pasta / "alunos_aprovados.xlsx", index=False)
print("\nExportado com sucesso: alunos_aprovados.xlsx")
