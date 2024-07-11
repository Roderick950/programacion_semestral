def prog2():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = float(input("Ingrese la cantidad del producto: "))
    impuesto = precio * cantidad * 0.07
    total = precio * cantidad + impuesto
    print(f"El total, incluyendo el impuesto del 7%, es: {total:.2f}")

