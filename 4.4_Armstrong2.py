numero = int(input("Ingrese un número positivo: "))
copiaNumero = numero
i = 0
#suma = 0
suma = 0
j = 0

while copiaNumero != 0:
		ultimaCifra = copiaNumero % 10
		copiaNumero = copiaNumero // 10

		i = i + 1

while j < i:
	numero = str(numero)
	suma = suma + (int(numero[j])**i)

	j = j + 1

#print(suma2)

if suma == int(numero):
	print("El número ingresado es un número de Armstrong")
else:
	print("El número ingresado NO es un número de Armstrong")