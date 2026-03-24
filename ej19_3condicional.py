#Usá una prueba condicional en la declaración while para detener el loop.
while True:
    edad = int(input("Ingrese su edad (escribir -1 para salir): "))
    if edad == -1:
        print("¡Gracias por usar el sistema de entradas del cine!")
        break
    if edad < 3:
        print("¡Entrada gratis!")
    elif 3 <= edad <= 12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")