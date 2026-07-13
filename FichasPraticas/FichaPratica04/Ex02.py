vendas = [120, 150, 90, 200, 175, 300, 250, 130, 160, 95, 210, 180, 320, 280]
dias = [
    "Segunda 1", "Terca 1", "Quarta 1", "Quinta 1", "Sexta 1", "Sabado 1", "Domingo 1",
    "Segunda 2", "Terca 2", "Quarta 2", "Quinta 2", "Sexta 2", "Sabado 2", "Domingo 2",
]

total_vendido = sum(vendas)
media_diaria = total_vendido / len(vendas)
indice_melhor_dia = vendas.index(max(vendas))
indice_pior_dia = vendas.index(min(vendas))
dias_acima_media = [dia for dia, venda in zip(dias, vendas) if venda > media_diaria]

print(f"Total vendido: {total_vendido:.2f} EUR")
print(f"Media diaria: {media_diaria:.2f} EUR")
print(f"Melhor dia: {dias[indice_melhor_dia]} ({vendas[indice_melhor_dia]} EUR)")
print(f"Pior dia: {dias[indice_pior_dia]} ({vendas[indice_pior_dia]} EUR)")
print(f"Dias acima da media: {len(dias_acima_media)}")

print("\nClassificacao diaria:")
for dia, venda in zip(dias, vendas):
    if venda < 120:
        classificacao = "Vendas baixas"
    elif venda <= 199:
        classificacao = "Vendas medias"
    else:
        classificacao = "Vendas altas"

    print(f"{dia}: {venda} EUR - {classificacao}")

print("\nInterpretacao:")
print("Os fins de semana apresentam vendas mais fortes, sobretudo aos sabados.")
print("Existem dias bastante acima dos restantes, como os sabados e domingos.")
print("A loja deve reforcar stock e equipa nos fins de semana.")
