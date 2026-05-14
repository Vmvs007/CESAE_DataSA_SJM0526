def maior_de_idade(idade:int):

    if idade >= 18:
        return True
    else:
        return False


def fase_vida(idade:int):

    if idade >=64:
        return "Idoso"
    elif idade >=18:
        return "Adulto"
    elif idade >= 12:
        return "Adolescente"
    elif idade >=0:
        return "Criança"
    else:
        return "Indefinido/Erro"
    

def capital_pais(pais):

    if pais == "Portugal":
        return "Lisboa"
    elif pais == "Espanha":
        return "Madrid"
    elif pais == "França":
        return "Paris"
    elif pais == "Itália":
        return "Roma"
    elif pais == "Alemanha":
        return "Berlim"
    else:
        return "País não encontrado"
    
