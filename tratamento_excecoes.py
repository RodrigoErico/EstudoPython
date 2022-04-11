try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número para dividir com o primeiro: '))
    n = a / b
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except ValueError:
    print('Tivemos um problema com os dados fornecidos')
except KeyboardInterrupt:
    print('O usuário interrompeu a execução do programa')
else:
    print(n)
