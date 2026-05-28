from FichaPratica02.Ex02.Edificio import Edificio

edificio1 = Edificio(nome="Edifício Universal",
                     rua="Rua dos Canteiros",
                     cidade="Porto",
                     cor_fachada="Branca",
                     num_andares=5,
                     tem_garagem=True)

print(edificio1.get_nome())
print(edificio1.get_rua())
print(edificio1.get_cidade())
print(f"Cor Fachada: {edificio1.get_cor_fachada()}")
print(f"Num. Andares: {edificio1.get_num_andares()}")
print(f"Tem garagem? {edificio1.get_tem_garagem()}\n")

# Trocar a cor
edificio1.set_cor_fachada("Amarela")

print(edificio1.get_nome())
print(edificio1.get_rua())
print(edificio1.get_cidade())
print(f"Cor Fachada: {edificio1.get_cor_fachada()}")
print(f"Num. Andares: {edificio1.get_num_andares()}")
print(f"Tem garagem? {edificio1.get_tem_garagem()}\n")
