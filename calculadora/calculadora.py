def calculadora():
    print("--- Calculadora en Python ---")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

    while True:
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif opcion == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif opcion == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre cero.")
            except ValueError:
                print("Error: Por favor, ingresa solo números.")
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    calculadora()