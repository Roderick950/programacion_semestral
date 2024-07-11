def prog27():     
    print("Determinar si un numero es divisible entre 3 y 5")

    Num = float(input("Ingrese un número: "))

    print('\n')

    if Num  % 3 == 0 and Num % 5 == 0: 
        print("Es divisible entre 3 y 5")

    elif Num % 3 == 0:
        print("Es divisible entre 3")

    elif Num % 5 == 0: 
         print("Es divisible entre 5")
         
    else: 
          print("El número no es divisible")

