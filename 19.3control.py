while True:
    cantidad = int(input("¿Cuántas ingredientes querés pedir?: "))
    if cantidad <= 0:
        print("¡Gracias por usar el sistema de pedidos de pizza!")
        break
    elif cantidad >= 1:
        for i in range(cantidad):
            ingrediente = input(f"Ingrediente {i + 1}: ")
            print(f"Agregaste {ingrediente} a tu pizza.")
        print("¡Tu pizza está lista para ser horneada!")
        break