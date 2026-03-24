from pathlib import Path
path = Path("guest_book.txt")
while True:
    nombre = input("¿Cuál es tu nombre? (Escribí 'salir' para terminar) ")
    if nombre.lower() == 'salir':
        break
    with open(path, "a") as file:
        file.write(nombre + "\n")