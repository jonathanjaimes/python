"""
while True:
    sumar = 0
    n = int(input("Ingrese un número: "))
    sumar = sumar+n
    operador = input("Ingrese un operador: ")
    n = int(input("Ingrese un número: "))
    if operador == "*":
        resultado = sumar*n
    if operador == "+":
        resultado = sumar+n
    if operador == "-":
        resultado = sumar-n
    if operador == "/":
        resultado = sumar/n
    print(resultado)
    comando = input("Ingrese el igual: ")
    if comando == "=":
        print(resultado)
"""

a = int(input())

suma = a

while True:
    
    operador = input()

    if operador == "*":
        b = int(input())
        suma = suma * b
    if operador == "+":
        b = int(input())
        suma = suma + b
    if operador == "-":
        b = int(input())
        suma = suma - b
    if operador == "/":
        b = int(input())
        suma = suma / b

    if operador == "=":
    	break

    print(f"Resultado parcial: {suma}")

print(f"La cantidad calculada es: {suma}")