def litrosAgua ():
    cantidadLitros = float(input("Por favor, ingrese la cantidad de litros de agua: "))
    
    if cantidadLitros <= 250:
        llave = "abierta"
        
    elif cantidadLitros >= 450:
        llave = "cerrada"
    
    else:
        llave = "cerrada"
    
        
    print(f"Señor usuario, ud debe tener su llave {llave}")
    

litrosAgua()

