def prog35():       
    print("Tabla de multiplicar ")

    n = int(input("Introduce un número entero positivo: "))

    while n  <= 0:
        print("Error: Debes introducir un número entero positivo.")
        n  = int(input("Introduce un número entero positivo: "))

    print(f"Tabla de multiplicar del {n }:")
    for i in range(1, 11):
        resultado = n  * i
        print(f"{n } x {i} = {resultado}")
