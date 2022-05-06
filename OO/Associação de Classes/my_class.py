from typing import Type


class Interruptor:

    def __init__(self, comodo: str):
        self.__comodo = comodo

    def acender(self):
        # print('acendendo {}'.format(self.__comodo))
        print(f'acendendo {self.__comodo}')

    def apagar(self):
        print(f'apagando {self.__comodo}')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


ana = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_sala = Interruptor('sala')

ana.acender_luz(interruptor_sala)
ana.apagar_luz(interruptor_sala)

ana.acender_luz(interruptor_quarto)
ana.apagar_luz(interruptor_quarto)
ana.dormir()
