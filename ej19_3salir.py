while True:
    edad = input("Ingrese su edad(escribir 'salir' para salir): ")
    if edad == "salir":
        print("¡Gracias por usar el sistema de entradas del cine!")
        break
    edad = int(edad)
    if edad < 3:
        print("¡Entrada gratis!")
    elif 3 <= edad <= 12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")