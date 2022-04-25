class Pessoa:           # substantivo => Classe
  
  def __init__(self, name: str, age: int) -> None:
    self.name = name    # substantivo => Atributo
    self.age = age      # substantivo => Atributo
    
  def drive(self, vehicle: str) -> None:              # verbos => Métodos
    print('Dirigir um {}' .format(vehicle))
    
  def sing(self) -> None:                        # verbos => Métodos
    print('Lalalala')
    
  def present_age(self) -> int:                 # verbos => Métodos
    return self.age