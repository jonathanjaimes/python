def descuentoTipo():
    
      #print("Por favor, escoja el número que coincide con el tipo de artículo que desea comprar: ")
    print("1 - Textil")
    print("2 - Electrodoméstico")
    print("3 - Elementos de cocina")
    print("4 - Videojuegos")
    opcion = int(input("Ingrese el número que corresponda con el tipo de artículo que desea comprar: "))
    valorSinDescuento = float(input("Ingrese el valor del artículo que desea comprar: "))

    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print("El valor ingresado para el tipo de producto es inválido")
        print()
        
        print("1 - Textil")
        print("2 - Electrodoméstico")
        print("3 - Elementos de cocina")
        print("4 - Videojuegos")
        opcion = int(input("Ingrese el número que corresponda con el tipo de artículo que desea comprar: "))
        valorSinDescuento = float(input("Ingrese el valor del artículo que desea comprar: "))

    if opcion == 1:
        
        nuevoValor = valorSinDescuento
    
    elif opcion == 2:
        
        nuevoValor = valorSinDescuento - (valorSinDescuento*0.037)

    elif opcion == 3:
        nuevoValor = valorSinDescuento - (valorSinDescuento*0.042)
        
    elif opcion == 4:
        nuevoValor = valorSinDescuento - (valorSinDescuento*0.078)

        
    print(f"El valor de su compra es: {nuevoValor}")

descuentoTipo()