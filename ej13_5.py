frutas_favoritas = ["manzana", "banana", "naranja"]
for i in range(3):
    frutas_favoritas_usuario = input("¿Cuáles son tus frutas favoritas? ")
    if frutas_favoritas_usuario in frutas_favoritas:
        print(f"Te gusta la {frutas_favoritas_usuario} como a mí!")