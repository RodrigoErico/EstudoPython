# Imposto cobra é de 30% sobre o valor do salario

salario = 1000

def calcular_imposto(salario):
    return salario * 0.3

print(calcular_imposto(salario))


# Função lambda
preco = 1200

calcular_imposto_02 = lambda preco: preco * 0.3
print(calcular_imposto_02(preco))