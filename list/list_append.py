# Criar uma lista com a lista criada
lista_01 = [
    [1, 2, 3],
    ['agua','leite','arroz'],
    [2, 5, 10]
]

lista_total = []

for sub_lista in lista_01:
    for item in sub_lista:
        lista_total.append(item)

print(lista_total)


# Feito com uma função

lista_02 = [
    [11, 23, 32],
    ['agua','leite','arroz'],
    [2, 5, 10]
]

def flatten_list(lista_02):
    return [i for sub_l in lista_02 for i in sub_l]

segunda_lista = flatten_list(lista_02)
print(segunda_lista)