class Car():

    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

    def modo_turbo(self):
        print('Ativar modo turbo')


primeiro_carro = Car('Ford', 'Ranger', 'Preto', 'Diesel')
print(primeiro_carro.combustivel)

primeiro_carro.modo_turbo()

# Função modo turbo é um método. Ele executa alguma coisa.
