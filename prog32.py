def prog32():      
    print('programa que suma numeros hasta un limite')
    limite = 100
    suma = 0

    while suma < limite:
        numero = int(input("Introduce un número entero: "))
        if numero > 0:
            suma += numero 
          
        else:
            print("Por favor, introduce otro número entero")

    print(f"Se ha alcanzado o superado el límite de {limite}. La suma total es: {suma}")

        



