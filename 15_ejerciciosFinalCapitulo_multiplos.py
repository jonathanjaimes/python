

numero = int(input("Ingrese un número: "))

#Pregunta, si el número es multiplo de tres, quedese quieto.
if numero%3 == 0:
	pass

#Si no es múltiplo de tres, transformese en el múltiplo de tres mayor más cercano
else:
	mod = numero%3
	numero = numero - mod
	numero = numero + 3

#Al múltiplo de tres, sumarle treinta

numero = numero + 30

#empieza restando tres desde el inicio, es el equivalente a en el punto anterior haberle sumado 27
#que es la cantidad que separa el primer múltiplo del último en diez multiplos.

for i in range(1, 11):
	numero = numero - 3 
	print(numero)
