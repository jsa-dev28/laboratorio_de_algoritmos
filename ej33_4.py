while True:
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")