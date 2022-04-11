num = {
    '1' : 'um',
    '2' : 'dois',
    '3' : 'tres',
    '4' : 'quatro'
}

number = input('Digite os numeros: ')

output = ''

for digito in number:
    output = output + num.get(digito, '?') + ' ' # '?' subtitui quando nao a o digito na variavel num
    
print(output)