def cuadratica():
    
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    
    x1 = (-b+(b**2-4*a*c)**(1/2))/2*a
    x2 = (-b-(b**2-4*a*c)**(1/2))/2*a
    
    discriminante = (b**2-4*a*c)**(1/2)
    
    if discriminante >= 0 and a != 0:
        print(f"La ecuación tiene solución y su solución es x1={x1} y x2={x2}")
    
    else:
        print("La ecuación no tiene solución")
        
cuadratica()