from Calculate import Calculate

calcular = Calculate #Instancia de la clase 

operations = []

with open ('C:/Users/SENA/Desktop/Python/Operations.txt','r') as archive:
  for linea in archive:
    separar = linea.split(' ')
    operations.append(separar)

#Funcion que valida los numeros si son enteros o decimales
def validate (num1,num2):
  if '.' in num1 or '.' in num2:
    return print(calcular.sumar(float(num1),float(num2)))
  else:
    return print(calcular.sumar(int(num1),int(num2)))

for iterador in operations:
  """ if iterador[1] == '+':
    print("==== SUMA ===")
    validate(iterador[0],iterador[2])
  
  elif iterador[1] == '-':
    print("==== RESTA ===")
    validate(iterador[0],iterador[2])
  
  elif iterador[1] == '*':
    print("==== MULTIPLICACIÓN ===")
    validate(iterador[0],iterador[2])
  
  elif iterador[1] == '/':
    print("==== DIVISIÓN ===")
    validate(iterador[0],iterador[2])"""

  if iterador[1] == '^':
    print("==== MODULO ===")
    if '-' in iterador[0] and '.' in iterador[2]:
      print(calcular.potencia(iterador[0],iterador[2]))


