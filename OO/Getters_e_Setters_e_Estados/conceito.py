"""
  Métodos setter e getter:
  * Métodos Setter: usados para alterar ou inserir valores nos membros de dados.
  Ex: setNome(), setDataNascimento()
  
  * Métodos Getter: usados para recuperar(Ler) valores armazenados nos objetos.
  Ex: getNome, getDataNascimento
  
  Como regra, um objeto só pode ter seus dados manippulados com o uso de setters
  e getters especificados.
"""

class Conceito():
  def __init__(self, valor):
    self.x = valor
  
  '''Método getter para retornar o valor do atributo x '''
  def get_valor(self):
    return self.x
  
  '''Método setter para atribuir um novo valor ao atributo x '''
  def set_valor(self, v):
    self.x = v
    
objeto = Conceito(12)
print('Valor do objeto: ', objeto.get_valor())

val = int(input('Digite um número: '))
objeto.set_valor(val)
print('Valor do objeto após atribuição: ', objeto.get_valor())
  