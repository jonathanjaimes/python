while True:

	m = int(input("Ingrese un número: "))
	n = int(input("Ingrese un número mayor al número ingresado: "))

	if m < n:
		break

acumPares = 0
acumImpares = 0

for x in range(m, n+1):
	if x%2 == 0:
		acumPares = acumPares + x

	if x%2 != 0:
		acumImpares = acumImpares + x

print(f"En el rango de {m} hasta {n} la suma de los números pares es de {acumPares}")
print(f"En el rango de {m} hasta {n} la suma de los números pares es de {acumImpares}")