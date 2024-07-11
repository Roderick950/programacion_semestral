def prog37():
    print("Contar vocales en una cadena \n")

    c = input("Ingresa una cadena de texto: ")

    vocales = "aeiouAEIOU"

    contador_vocales = 0

    for caracter in c:
        if caracter in vocales:
            contador_vocales += 1

    print(f"El número de vocales que hay en la cadena {c} es: {contador_vocales}")

