def prog42():    
    print("Dibujar un triángulo de asteriscos \n")

    N = int(input("Ingresa un número entero positivo para la altura del triángulo: "))

    while N <= 0:
        print("Error: Debes introducir un número entero positivo")
        N = int(input("Ingresa un número entero positivo para la altura del triángulo: "))


    for i in range(1, N + 1):
        print('*' * i)
