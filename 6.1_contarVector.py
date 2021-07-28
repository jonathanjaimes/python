"""	
while True:
	num1 = int(input("Ingrese un número: "))
	if num1 >= 10 and num1 <= 20:
		break

	
while True:
	num2 = int(input("Ingrese un número: "))
	if num2 >= 10 and num2 <= 20:
		break

	
while True:
	num3 = int(input("Ingrese un número: "))
	if num3 >= 10 and num3 <= 20:
		break

	
while True:
	num4 = int(input("Ingrese un número: "))
	if num4 >= 10 and num4 <= 20:
		break


vector = num1, num2, num3, num4

suma = 0
for i in range(0, 4):
	if vector[i] == 14:
		suma = suma + 1

print(f"El número 14 aparece en el vector {suma} veces")

print()


a = ("casa", "carro", "beca")
b = ("amarillo", "azul", "rojo")

for tipo, color in zip(a, b):
	print(tipo, color)

"""

lista = []



while True:
	num1 = int(input("Ingrese un número: "))
	if num1 >= 10 and num1 <= 20:
		break
lista.append(num1)

while True:
	num2 = int(input("Ingrese un número: "))
	if num2 >= 10 and num2 <= 20:
		break
lista.append(num2)

while True:
	num3 = int(input("Ingrese un número: "))
	if num3 >= 10 and num3 <= 20:
		break
lista.append(num3)

while True:
	num4 = int(input("Ingrese un número: "))
	if num4 >= 10 and num4 <= 20:
		break
lista.append(num4)


suma = 0
for i in range(0, len(lista)):
	if lista[i] == 14:
		suma = suma + 1

print(f"El número de veces que se repite el número 14 es {suma}")