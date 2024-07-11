def prog14():         
    print('programa que verifica si una palabra tiene cinco letras')
    Palabra = str(input("Ingresa una palabra: "))

    cant_palabra = len(Palabra[:10])

    if cant_palabra > 5:
        print("La palabra tiene mas de 5 letras") 

    else:
        print("La palabra tiene menos de 5 letras")
            
