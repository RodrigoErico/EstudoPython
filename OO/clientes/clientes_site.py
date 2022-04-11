# Criar uma classe para clientes 
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome 
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')
     
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')
     
            
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Faça upgrade para Premium para ver esse filme.')
        else:
            print('Plano inválido')    
            
            
            
client = Cliente('Rodrigo', 'rodrigo@gmail.com', 'Basic')
print(client.plano)
client.ver_filme('Harry Potter', 'Premium')


client.mudar_plano('Premium')
print(client.plano)
client.ver_filme('Harry Potter', 'Premium')
