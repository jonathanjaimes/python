
#Nos aseguramos que el número ingresado esté en el rango de aceptación.

while True:
	numero = int(input("Ingrese un número de cero a 99: "))
	if numero >= 0 and numero <= 99:
		break

#creamos las listas, las primeras tres nos permiten buscar el número de cero a 29 directamente, de treinta en adelante buscaremos las dos partes del número
#una primera parte está en la lista4 en donde se encuentran las decenas, y en la lista uno buscaremos las unidades.

lista1 = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
lista2 = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciochi", "diecinueve"]
lista3 = ["veinte", "veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiseis", "veintisiete", "veintiocho", "veintinueve"]
lista4 = ["treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

if numero >= 0 and numero <= 9:

	for i in range(0, len(lista1)):
		if numero == i:
			print(lista1[i])

if numero >= 10 and numero <= 19:

	for i in range(0, len(lista2)):
		if numero == i+10:
			print(lista2[i])

if numero >= 20 and numero <= 29:

	for i in range(0, len(lista3)):
		if numero == i+20:
			print(lista3[i])

#De aquí para atrás usamos las tres primeras listas de forma directa.
#De aqúí en adelante descomponemos el número en sus cifras constitutivas, el primer número lo buscamos en la lista de las decenas
# y el segundo número lo buscamos en la lista de las unidades. Por último contatenamos e imprimimos.

if numero >= 30 and numero <= 99:

	cifra1 = numero//10
	cifra2 = numero%10

	for i in range(0, len(lista4)):
		if cifra1 == i+3:
			primerNum = lista4[i]

	for i in range(0, len(lista1)):
		if cifra2 == i:
			segNum = lista1[i]

	print(f"{primerNum} y {segNum}")