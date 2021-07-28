

num = int(input("Ingrese un numero: "))

def primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
            
        else:
            return True
            

resultado = primo(num)

if resultado is True:
    print("El número es primo")

else:
    print("El numero no es primo")



primo(num)