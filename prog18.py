def prog18():         
    print('determina si un caracter es una letra o un digito')
    caracter = input("Ingresa un caracter: ")

    if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
        print("Letra")
        
    if '0' <= caracter <= '5': 
        print("Digito")
