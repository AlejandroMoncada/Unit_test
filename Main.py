from Calculate import Calculate

calcular = Calculate #Instancia de la clase 

operations = []
row = 0

with open ('C:/Users/SENA/Desktop/Python/Operations.txt','r') as archive:
  for linea in archive:
    separar = linea.split(' ')
    operations.append(separar)

for iterador in operations:
  row+=1
  if iterador[1] == '+':
    result = calcular.sumar(float(iterador[0]),float(iterador[2]))
    if result == float(iterador[3]):
      print(row,'Pasa la prueba')
    else:
      print(row,"No paso la prueba, se esperaba",iterador[3],'y llego:',result)
  
  elif iterador[1] == '-':
    result = calcular.restar(float(iterador[0]),float(iterador[2]))
    if result == float(iterador[3]):
      print(row,'Pasa la prueba')
    else:
      print(row,"No paso la prueba, se esperaba",iterador[3],'y llego:',result)

  
  elif iterador[1] == '*':
    result = calcular.multiplicar(float(iterador[0]),float(iterador[2]))
    if result == float(iterador[3]):
      print(row,'Pasa la prueba')
    else:
      print(row,"No paso la prueba, se esperaba",iterador[3],'y llego:',result)

  
  elif iterador[1] == '/':
    result = calcular.division(float(iterador[0]),float(iterador[2]))
    if result == float(iterador[3]):
      print(row,'Pasa la prueba')
    else:
      print(row,"No paso la prueba, se esperaba",iterador[3],'y llego:',result)


  # if iterador[1] == '^':
  #   result = calcular.potencia(float(iterador[0]),float(iterador[2]))
  #   if str(result) == iterador[3]:
  #     print(row,'Pasa la prueba')
  #   elif str(result) != iterador[3]:
  #     print(row,"No paso la prueba, se esperaba",iterador[3],'y llego:',result)


