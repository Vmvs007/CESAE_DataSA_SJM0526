import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 160

zonas = [
    "Costa Norte",
    "Costa Sul",
    "Zona Portuária",
    "Reserva Natural",
    "Falésias",
    "Praia Urbana"
]

tipos_missao = [
    "Patrulhamento",
    "Mapeamento",
    "Monitorização Ambiental",
    "Apoio a Salvamento"
]

operadores = [
    "Ana Silva",
    "Bruno Costa",
    "Carla Sousa",
    "Diogo Martins",
    "Inês Rocha",
    "Miguel Alves",
    "Rita Fernandes"
]

modelos = [
    "Aero X1",
    "Falcon Pro",
    "SeaWatch"
]

datas = (
    pd.Timestamp("2026-01-01")
    + pd.to_timedelta(rng.integers(0, 181, n), unit="D")
)

horas = rng.integers(6, 21, n)

zona = rng.choice(
    zonas,
    n,
    p=[0.18, 0.17, 0.17, 0.18, 0.14, 0.16]
)

tipo = rng.choice(
    tipos_missao,
    n,
    p=[0.30, 0.23, 0.30, 0.17]
)

operador = rng.choice(operadores, n)
modelo = rng.choice(modelos, n, p=[0.38, 0.34, 0.28])

distancia = np.round(
    np.clip(rng.gamma(2.6, 3.5, n) + 1.5, 1.5, 24),
    1
)

vento = np.round(
    np.clip(rng.normal(18, 7, n), 3, 42),
    1
)

temperatura = np.round(
    np.clip(rng.normal(20, 5, n), 8, 34),
    1
)

bonus_duracao = np.select(
    [
        tipo == "Apoio a Salvamento",
        tipo == "Mapeamento",
        tipo == "Monitorização Ambiental"
    ],
    [18, 12, 8],
    default=4
)

duracao = np.round(
    10
    + distancia * 3.1
    + vento * 0.45
    + bonus_duracao
    + rng.normal(0, 7, n)
).astype(int)

duracao = np.clip(duracao, 15, 145)

bateria_inicial = rng.integers(84, 101, n)

bonus_consumo = np.select(
    [
        modelo == "Aero X1",
        modelo == "Falcon Pro",
        modelo == "SeaWatch"
    ],
    [5, 1, 3],
    default=0
)

consumo = np.round(
    6
    + distancia * 2.1
    + vento * 0.35
    + bonus_consumo
    + rng.normal(0, 4, n),
    1
)

consumo = np.clip(consumo, 8, 82)

bateria_final = np.round(
    np.clip(bateria_inicial - consumo, 4, 96),
    1
)

imagens = np.round(
    duracao * rng.uniform(3.8, 5.6, n)
    + rng.normal(0, 35, n)
).astype(int)

imagens = np.clip(imagens, 30, None)

risco_zona = np.select(
    [
        zona == "Reserva Natural",
        zona == "Zona Portuária",
        zona == "Praia Urbana"
    ],
    [1.4, 1.1, 0.8],
    default=0.5
)

alertas = rng.poisson(
    risco_zona
    + np.where(tipo == "Monitorização Ambiental", 1.2, 0.2)
)

prob_incidente = np.clip(
    0.10
    + np.maximum(vento - 18, 0) / 45
    + np.maximum(18 - bateria_final, 0) / 35,
    0.05,
    0.85
)

incidentes = rng.binomial(2, prob_incidente)

estado = np.where(
    (bateria_final < 15)
    | (vento > 36)
    | (incidentes >= 2),
    "Interrompida",
    "Concluída"
)

interrupcoes_aleatorias = rng.choice(
    np.arange(n),
    size=8,
    replace=False
)

estado[interrupcoes_aleatorias] = "Interrompida"

bonus_custo = np.select(
    [
        tipo == "Apoio a Salvamento",
        tipo == "Mapeamento",
        tipo == "Monitorização Ambiental"
    ],
    [35, 18, 14],
    default=8
)

custo = np.round(
    15
    + duracao * 0.68
    + distancia * 1.5
    + incidentes * 20
    + bonus_custo
    + rng.normal(0, 6, n),
    2
)

df_missoes = pd.DataFrame({
    "Missao_ID": [f"M{i:04d}" for i in range(1, n + 1)],
    "Data": datas.strftime("%Y-%m-%d"),
    "Hora_Inicio": [f"{h:02d}:00" for h in horas],
    "Zona": zona,
    "Tipo_Missao": tipo,
    "Operador": operador,
    "Drone_Modelo": modelo,
    "Distancia_km": distancia,
    "Duracao_Min": duracao,
    "Vento_kmh": vento,
    "Temperatura_C": temperatura,
    "Bateria_Inicial": bateria_inicial,
    "Bateria_Final": bateria_final,
    "Imagens_Captadas": imagens,
    "Alertas_Ambientais": alertas,
    "Incidentes_Tecnicos": incidentes,
    "Estado_Missao": estado,
    "Custo_Estimado_EUR": custo
})

# Diferenças de escrita intencionais
df_missoes.loc[12, "Zona"] = "costa norte"
df_missoes.loc[66, "Zona"] = "Costa  Sul "
df_missoes.loc[103, "Zona"] = "zona portuária"

# Valores em falta intencionais
df_missoes.loc[[7, 54, 119], "Vento_kmh"] = np.nan
df_missoes.loc[[22, 88], "Bateria_Final"] = np.nan
df_missoes.loc[[31, 77], "Operador"] = np.nan

# Valores anómalos intencionais
df_missoes.loc[90, "Duracao_Min"] *= 2
df_missoes.loc[90, "Custo_Estimado_EUR"] *= 1.7
df_missoes.loc[130, "Bateria_Final"] = (
    df_missoes.loc[130, "Bateria_Inicial"] + 5
)

# Registos duplicados intencionais
df_missoes = pd.concat(
    [
        df_missoes,
        df_missoes.iloc[[4, 47]]
    ],
    ignore_index=True
)

df_missoes.to_csv(
    "missoes_drones_costeiros.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Ficheiro criado com sucesso.")
print(df_missoes.shape)