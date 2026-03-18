while True:
    edad = int(input("Ingrese su edad: "))
    if edad < 3:
        print("¡Entrada gratis!")
    elif 3 <= edad <= 12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")