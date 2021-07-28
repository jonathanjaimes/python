def descuentoRango():
    valor = float(input("Por favor, ingrese el valor del artículo deseado: "))
    
    if valor >= 0 and valor <= 100000:
        descuento = 0
    elif valor > 100000 and valor <= 225000:
        descuento = 0.015
    elif valor > 225000 and valor <= 375000:
        descuento = 0.038
    elif valor > 375000:
        descuento = 0.103
        
    print(f"El valor de su artículo es: {valor - (valor*descuento)}")
    
descuentoRango()