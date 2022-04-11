senha = input('Digite a senha: ')

if len(senha) < 6 or len(senha) > 10:
    print('não é valida')
else:
    print('Senha valida')
