import random

# faça um programa que gere um numero aleatorio e vc precisa adivinhar o numero
# que sera apresentado e tera 3 tentativas

num_aleatorio = random.randint(1, 10)
num_tentativas = 0

while num_tentativas < 3:
    num_tentativas += 1
    num_resposta = int(input('Digite o número: '))
    if num_resposta == num_aleatorio:
        print('Vc acertou, o numero é', num_aleatorio)
        break
else:
    print('Vc errou o número era', num_aleatorio)

        
