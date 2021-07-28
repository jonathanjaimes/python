while True:
  numero = int(input("Ingrese un número entre uno y veinte: "))
  if numero > 0 and numero < 21:
    break

def primoFunc(numero):

  bandera = True  
  
  for i in range(2, numero):
    modu = numero%i
    if modu == 0:
      bandera = False
      break

  if bandera == True:
    print("El número es primo")
    
  else:
    print("El numero no es primo")

primoFunc(numero)