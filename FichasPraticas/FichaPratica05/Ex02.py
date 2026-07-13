import numpy as np


vendas = np.array([
    [10, 5, 8, 12],
    [15, 7, 6, 10],
    [12, 6, 9, 14],
    [20, 10, 12, 18],
    [18, 9, 11, 16],
    [14, 8, 10, 15],
    [22, 11, 13, 20],
])

precos = np.array([5.0, 7.5, 3.0, 4.5])

total_por_produto = np.sum(vendas, axis=0)
total_por_dia = np.sum(vendas, axis=1)
produto_mais_vendido = np.argmax(total_por_produto) + 1
dia_maior_vendas = np.argmax(total_por_dia) + 1
media_diaria = np.mean(total_por_dia)
dias_acima_media = np.where(total_por_dia > media_diaria)[0] + 1
faturacao_diaria_produto = vendas * precos
faturacao_total_semana = np.sum(faturacao_diaria_produto)
faturacao_por_produto = np.sum(faturacao_diaria_produto, axis=0)
produto_maior_faturacao = np.argmax(faturacao_por_produto) + 1

print("Vendas:")
print(vendas)
print(f"Total por produto: {total_por_produto}")
print(f"Total por dia: {total_por_dia}")
print(f"Produto mais vendido: Produto {produto_mais_vendido}")
print(f"Dia com maior total de vendas: Dia {dia_maior_vendas}")
print(f"Media diaria de vendas: {media_diaria:.2f}")
print(f"Dias acima da media: {dias_acima_media}")
print("Faturacao diaria por produto:")
print(faturacao_diaria_produto)
print(f"Faturacao total da semana: {faturacao_total_semana:.2f} EUR")
print(f"Produto com maior faturacao: Produto {produto_maior_faturacao}")

print("\nInterpretacao:")
if produto_mais_vendido == produto_maior_faturacao:
    print("O produto mais vendido tambem foi o mais rentavel.")
else:
    print("O produto mais vendido nao foi o mais rentavel, porque o preco tambem influencia a faturacao.")
