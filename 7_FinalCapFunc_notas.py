def ingresoNotas():

  while True:
    nota1 = float(input("Ingrese su primera nota: "))
    if nota1 >= 0 and nota1 <= 5:
      break
  while True:
    nota2 = float(input("Ingrese su segunda nota: "))
    if nota2 >= 0 and nota2 <= 5:
      break
  while True:
    nota3 = float(input("Ingrese su tercera nota: "))
    if nota3 >= 0 and nota3 <= 5:
      break
  while True:
    nota4 = float(input("Ingrese su cuarta nota: "))
    if nota4 >= 0 and nota4 <= 5:
      break
  while True:
    nota5 = float(input("Ingrese su quinta nota: "))
    if nota5 >= 0 and nota5 <= 5:
      break

  

  return nota1, nota2, nota3, nota4, nota5


nota1, nota2, nota3, nota4, nota5 = ingresoNotas()

def promedio(nota1, nota2, nota3, nota4, nota5):

  notaFinal = (nota1 + nota2 + nota3 + nota4 + nota5) / 5  

  return notaFinal

notaFinal = promedio(nota1, nota2, nota3, nota4, nota5)

if notaFinal < 3.5:
  print(f"Has perdido la materia, tu promedio fue de {notaFinal}")
else:
  print(f"Has ganado la materia, tu promedio fue de {notaFinal}")