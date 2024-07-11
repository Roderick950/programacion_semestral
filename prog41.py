def prog41():    
    print("Convertir grados Celsius a Fahrenheit \n")

    i = int(input("Ingresa el inicio del rango en grados Celsius: "))
    f = int(input("Ingresa el fin del rango en grados Celsius: "))

   
    if i  > f:
        print("Error: El inicio del rango debe ser menor o igual al fin del rango")
    else:
        
        print("Tabla de conversión de Celsius a Fahrenheit:")
        print("Celsius\t\tFahrenheit")
        for celsius in range(i, f + 1):
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}\t\t{fahrenheit:.1f}")
