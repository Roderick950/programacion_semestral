import semestral

# Lista de archivos de módulos
files = [f"p{i}.py" for i in range(1, 43)]

def main():
    while True:
        print("\n\n 😄==== Menú ====😄")
        for i, filename in enumerate(files, start=1):
            print(f"{i}. Ejecutar función de {filename}")

        print("q. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        if choice.isdigit() and 1 <= int(choice) <= len(files):
            try:
                module_name = files[int(choice) - 1].rstrip(".py")
                module = _import_(module_name)
                module.run()  # Ejecutar la función 'run' del módulo
            except ImportError:
                print(f"No se pudo importar {module_name}. Verifica que el módulo existe y tiene la función 'run'.")
            except AttributeError:
                print(f"El módulo {module_name} no tiene la función 'run'.")
            except Exception as e:
                print(f"Error al ejecutar {module_name}: {e}")
            input("Presiona cualquier tecla para continuar...")
        elif choice == "q":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            input("Presiona cualquier tecla para continuar...")

if _name_ == "_main_":
    main()