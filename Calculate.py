class Calculate:
  def sumar (num1,num2):
    sum = num1 + num2
    return sum
  
  def restar (num1,num2):
    rest = num1 - num2
    return rest

  def multiplicar (num1,num2):
    multi = num1 * num2
    return multi
  
  def division (num1,num2):
    if num2 == 0:
      print("Operación no valida")
    divi = num1 / num2
    return divi

  def potencia (num1,num2):
    pote = pow(num1,num2)
    return pote
