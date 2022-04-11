number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplicar = list(map(lambda x : x * 2, number))
print(multiplicar)


# somar apenas se for o numero 5
cal = lambda list: [item + 1 if item == 5 else item for item in list]
print(cal([1, 2, 3, 4, 5]))


# string 

string = lambda nome, profissao: 'Profissional: ' + nome + ' ' + profissao
print(string('Rodrigo', 'Desenvolvedor'))