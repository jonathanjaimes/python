def resultadoFactorial():

    numero = (2*(n-1))
    contador = numero-1
    factorial = numero

    while contador != 0:
        factorial = factorial * contador
        #print(contador)
        contador = contador - 1

    return factorial


n = int(input("Ingrese la cantidad de términos a calcular: "))
x = int(input("Ingrese el valor de la x: "))
suma = 1

while n > 1:

    resultadoFactorial()

    result = (x**n)/resultadoFactorial()

    if n%2 != 0:
    	result = result * (-1)

    print(result)

    suma = suma + result 

    n = n - 1

print(f"La suma es: {suma}")