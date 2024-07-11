def prog3(): 
   print("calculo de imc de una persona ")
    peso = float(input("ingrese su peso en lb :"))
    altura = float(input("ingrese su altura:"))
    imc = (peso / altura **2)
    print(f"su indice de masa corporal es {imc}","lb")

