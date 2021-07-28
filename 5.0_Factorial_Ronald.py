factorial = int (input('Ingrese un número para saber su factorial (n!): '))

numAnterior = factorial
contador = factorial
multi = 1

while True:
  
  print (numAnterior, end = ' X ')
  multi = numAnterior * multi
  numAnterior -= 1
  contador -= 1
  
  if contador == 1:
      break
print (1,'=', multi)