import numpy as np


tempos_resposta = np.array([
    12, 15, np.nan, 20, 18,
    25, np.nan, 30, 22, 19,
])

print("Array original:")
print(tempos_resposta)

valores_em_falta = np.isnan(tempos_resposta)
quantidade_em_falta = np.sum(valores_em_falta)
media_sem_nan = np.nanmean(tempos_resposta)
mediana_sem_nan = np.nanmedian(tempos_resposta)

print(f"Valores em falta: {valores_em_falta}")
print(f"Quantidade de valores em falta: {quantidade_em_falta}")
print(f"Media ignorando valores em falta: {media_sem_nan:.2f}")
print(f"Mediana ignorando valores em falta: {mediana_sem_nan:.2f}")

tempos_corrigidos = np.where(valores_em_falta, media_sem_nan, tempos_resposta)

print("Array corrigido:")
print(tempos_corrigidos)
print(f"Nova media: {np.mean(tempos_corrigidos):.2f}")

print("\nInterpretacao:")
print("A media antes e depois da substituicao mantem-se igual, porque os valores em falta foram substituidos pela propria media.")
print("Como os dados nao parecem extremamente assimetricos, a media e aceitavel; se houvesse muitos extremos, a mediana seria mais robusta.")
