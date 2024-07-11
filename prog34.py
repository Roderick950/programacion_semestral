def prog34():       
    print("Convertir de decimal a binario \n")

    n_d = int(input("Introduce un número entero positivo: "))


    while n_d <= 0:
        print("Error: Debes introducir un número entero positivo")
        n_d = int(input("Introduce un número entero positivo: "))

    num_binario = ""
    cociente = n_d

    if cociente == 0:
        num_binario = "0"

    while cociente > 0:
        resto = cociente % 2
        num_binario= str(resto) + num_binario
        cociente = cociente // 2

    print(f"El número binario de {n_d} es: {num_binario}")
