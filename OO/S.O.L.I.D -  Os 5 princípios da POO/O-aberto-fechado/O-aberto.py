# Conceito aberto

class Decisao:

    def alternativas(self, tipo):
        tipo.decidir()


class Sair:

    def decidir(self):
        print('Vou sair de casa!')


class Ficar:

    def decidir(self):
        print('Vou ficar em casa!')


decisao = Decisao()
sair = Sair()
ficar = Ficar()

decisao.alternativas(sair)
