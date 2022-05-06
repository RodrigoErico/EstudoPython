# Conceito fechado
class Decisao:

    def alternativas(self, tipo):
        if tipo == 1:
            self.sair_de_casa()
        if tipo == 2:
            self.ficar_em_casa()

    def sair_de_casa(self):
        print('Vou sair de casa!')

    def ficar_em_casa(self):
        print('Vou ficar em casa!')


decisao = Decisao()
decisao.alternativas(1)
