def e_primo(num):
    if num <= 1:
        return False

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def e_perfeito(num):
    if num <= 1:
        return False

    soma_divisores = 0

    for divisor in range(1, num):
        if num % divisor == 0:
            soma_divisores += divisor

    return soma_divisores == num


def e_triangular(num):
    if num < 1:
        return False

    soma = 0
    contador = 1

    while soma < num:
        soma += contador
        contador += 1

    return soma == num
