def prog24():    
    print('programa que determina la categoria de un trbajador')
    exp_años = float(input("Ingresa tus años de experiencia: "))

    if exp_años < 2: 
        print("Junior")
        
    if  2 <= exp_años <= 5:
       print("Semi-senior")

    if exp_años > 10: 
        print("Senior")
