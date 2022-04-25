class Calculadora:
  
  def calcular(self, operacao, num1, num2):
    if operacao == '+':
      return self.__soma(num1, num2)
    elif operacao == '-':
      return self.__subtrair(num1, num2)
    else:
      print('Operação inválida')
      
  def __soma(self, num1, num2):
    return num1 + num2
  
  def __subtrair(self, num1, num2):
    return num1 - num2
  
calculadora = Calculadora()
resultado = calculadora.calcular('+', 2, 4)
print(resultado)