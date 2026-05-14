def converter_moedas(valor_euros,moeda_destino):

    if moeda_destino=="USD":
        return valor_euros*1.2
    elif moeda_destino=="GBP":
        return valor_euros*0.78
    elif moeda_destino=="BRL":
        return valor_euros*5.87
    else:
        return -1