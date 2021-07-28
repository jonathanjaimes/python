"""
multiplicando = int(input("Ingrese el primer numero: "))
multiplicador = int(input("Ingrese el segundo número: "))

contador = 0
producto = 0

while contador < multiplicador:

	producto = producto + multiplicando 
	contador = contador + 1 
	print(contador)

print(f"El producto es {producto}")

"""

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print()

contador1 = 0
producto1 = 1

while contador1 < exp-1:
	producto1 = producto1 * base
	contador1 += 1

#print(producto1)

veces = producto1

contador2 = 0

producto2 = 0

while contador2 < veces:
	producto2 = producto2 + base 
	contador2 = contador2 + 1 
	print(producto2)
print()
print(f"El resultado es: {producto2}")
