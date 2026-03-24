edad = input("¿Cuál es tu edad? ")
if edad.isdigit():
    edad = int(edad)
else:
    print("Por favor, ingresa un número válido para la edad.")
    exit()
if edad < 2:
    print("Es un bebé.")
elif edad >= 2 and edad < 4:
    print("Es un nene chico.")
elif edad >= 4 and edad < 13:
    print("Es un niño.")
elif edad >= 13 and edad < 20:
    print("Es un adolescente.")
elif edad >= 20 and edad < 65:
    print("Es un adulto.")
elif edad >= 65:
    print("Es un adulto mayor.")