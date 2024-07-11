def prog25():
    print("Clasificar el IMC en una persona")

    peso = float(input("Ingrese su peso: "))
    altura = float (input("Ingrese su altura: "))

    IMC = peso / (altura * altura)

    print("\n")

    if IMC < 18.5:
        Clasificación = "Bajo Peso"

    elif IMC >= 18.5 and IMC < 24.9:
         Clasificación = "Normal" 
        
    elif IMC >= 25 and IMC < 29.9: 
            Clasificación = "Sobrepeso"
            
    else: 
            Clasificación = "Obesidad"
            
    print(f'La persona tiene un IMC de {IMC: .2f}, lo que indica que su clasificacion es -{Clasificación}')
