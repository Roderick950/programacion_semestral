def prog23():    
    print('programa que verifica si un triangulo es valido')
    lado_1 = float(input("Ingresa la longitud del lado 1: "))
    lado_2 = float(input("Ingresa la longitud del lado 2: "))
    lado_3 = float(input("Ingresa la longitud del lado 3: "))

    longitud_xy = lado_1 + lado_2 

    if longitud_xy > lado_3: 
        print("La suma de los lados 1 y 2 es mayor que la longitud del lado 3")
        
    else: 
        print("La longitud del tercer lado es mayor")
