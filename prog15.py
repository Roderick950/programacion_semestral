def prog15():     
    print('programa que clasifica tu categoria de edad')
    Edad = float(input("Ingresa tu edad: "))

    if Edad >= 0 and Edad <= 12: 
        print("Infantil")
        
    elif Edad >= 13 and Edad <= 19:
        print("Adolescente")
        
    elif Edad >= 20 and Edad <= 59:
        print("Adulto")
        
    else: 
        print("Adulto Mayor")
