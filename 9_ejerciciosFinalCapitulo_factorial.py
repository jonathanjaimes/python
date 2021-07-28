#Ingresamos un número al que se le sacará el factorial.
while True:
    a = int(input("Ingrese un número: "))
    if a <= 50:
        break
#Permite guardar el número original recibido.
c = a


#Tenemos el valor de a, ahora vamos a hacer un recorrido que vaya desde a-1 hasta 1, 
#significa que b va a ir tomando los valores desde a-1 hasta 1.
for b in range(a-1, 0, -1):
        suma = 0

#Para cada valor de b, i va a hacer un recorrido tomando valores desde 1 hasta b.
#En otras palabras, va a sumar "a" tantas veces como diga b

        for i in range(1, b+1):
            suma = suma + a
        a = suma
#"a" va a ir actualizando sus valores conforme suma vaya incrementandose conforme b vaya haciendo
#su repectivo recorrido.
print(f"El factorial de {c} es {suma}")