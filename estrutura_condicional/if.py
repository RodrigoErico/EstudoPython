nota_aluno = int(input('Qual a sua nota? '))

if nota_aluno > 70 and nota_aluno < 90:
    print('Bom')
elif nota_aluno > 50 and nota_aluno < 70:
    print('Suficiente')
elif nota_aluno > 90:
    print('Muito bom')
else:
    print('Insuficiente')