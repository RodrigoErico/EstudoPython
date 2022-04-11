number = [12, 3, 40, 50, 45, 78, 120, 34, 3]

number.insert(0, 6)  # add numero 6 no começo da lista

number2 = number.copy()
number2.append(10)

print(number)
print(number2)

number3 = [12, 3, 120, 34, 120, 120]

print(number3.count(120))  # verifica quantas vezes o numero 120 existe na lista
print(number3.index(120))  # verifica o index do 120 na lista, mostra apenas o primeiro
