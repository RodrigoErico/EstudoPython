# Antes
'''
class SistemaCadastro:

  def register(self, name: str, age: int) -> None:
    if isinstance(name, str) and isinstance (age, int):  # verifica se é str e int.
      print('acessando o banco de dados...')
      print('Cadastrar o Usuário {}, Idade {}' .format(name, age))
    else:
      print('dados inválidos!')
'''
# Depois => Boas práticas

class RegistrationSystem:


    def register(self, name: str, age: int) -> None:
        if self.__validate_data(name, age):
            self.__save_users(name, age)
        else:
            print('dados inválidos!')
                     

    def __validate_data(self, name: str, age: int) -> bool:
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False


    def __save_users(self, name: str, age: int) -> None:
        print('Acessando o banco de dados...')
        print('Cadastrar o Usuário {}, Idade {}' .format(name, age))
