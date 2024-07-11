def prog11():    
    print("Determinar la edad de un adolescente")
    Edad = float(input("Ingrese la edad: "))

    print('\n')

    if (Edad > 12) and (Edad < 20):
        print("Adolescente")
        
    elif Edad < 12: 
        print("Niñx")
        
    else:
        print("Adulto")
        
   
