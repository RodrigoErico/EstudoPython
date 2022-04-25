class Pessoa:
  
  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.__cpf = cpf  # __cpf privado
    
  def beber(self, bebida): # publico
    if bebida == 'cerveja':
      self.__apresentar_cpf()
    print('bebendo...')
        
  def __apresentar_cpf(self): # encapsulamento privado
    print(self.__cpf)
  
identidade = Pessoa('Rodrigo', 31, '34555090')
identidade.beber('cerveja')
