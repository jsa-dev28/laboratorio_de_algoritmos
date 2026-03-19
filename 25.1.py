def hacer_sandwich(*ingredientes):
    print("Estás pidiendo un sándwich con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
hacer_sandwich('jamón', 'queso', 'lechuga')
hacer_sandwich('pollo', 'mayonesa')
hacer_sandwich('atún', 'tomate', 'cebolla', 'aceitunas')