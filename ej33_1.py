from pathlib import Path
path = Path("guest.txt")
nombre = input("¿Cuál es tu nombre? ")
path.write_text(nombre)