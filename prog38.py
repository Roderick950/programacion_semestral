def prog38():
    print("Imprimir números impares \n")
    n = int(input("Ingresa un número entero positivo: "))

    while n <= 0:
        print("Error: Debes introducir un número entero positivo")
        n = int(input("Ingresa un número entero positivo: "))


    print(f"Números impares del 1 al {n}:")
    for num in range(1, n + 1, 2):
        print(num)
