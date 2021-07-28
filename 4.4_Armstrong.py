numero = int(input("Ingrese un número positivo: "))

i = 0
suma = 0
suma2 = 0
j = 0
while i < len(str(numero)):
	numero = str(numero)
	suma = suma + int(numero[i])

	i = i + 1
#print(i)
while j < len(str(numero)):
	numero = str(numero)
	suma2 = suma2 + (int(numero[j])**i)

	j = j + 1

#print(suma2)

if suma2 == int(numero):
	print("El número ingresado es un número de Armstrong")
else:
	print("El número ingresado no es un número de Armstrong")