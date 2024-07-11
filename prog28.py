def prog28():     
    print("Verificar si un nombre es corto, mediano o largo")
    Nombre = str(input("Ingresa tu nombre: "))

    print('\n')

    cant_letras = len(Nombre)

    if cant_letras <= 5: 
        print("tu nombre es corto")
        
    elif cant_letras > 5 and cant_letras <= 8:  
        print("tu nombre es mediano")
        
    else: 
        print("tu nombre el largo")
     


