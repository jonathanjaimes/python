"""
Diseñe un algoritmo que reciba como dato de entrada 
un número entero perteneciente al sistema
decimal. Si cumple la condición de ser positivo, 
informe el número de cifras que posee, 
adicionalmente calcule la sumatoria de ellas; en 
caso contrario, imprima un mensaje que diga 
que el número no es positivo.
"""

numero = int(input("Ingrese un número positivo: "))

if numero >= 0:
	numero2 = str(numero)
	i = 0
	suma = 0
	while i < len(numero2):
		#print(numero2[i])
		
		suma = suma + int(numero2[i])
		i = i + 1
	print(f"La cantidad de cifras que posee el número ingresado es {i}")
	print(f"La suma de los digitos del número ingresado es: {suma}")

else:
	print("El número ingresado no es positivo.")

