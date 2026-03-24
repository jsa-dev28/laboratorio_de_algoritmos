pizzas = ["Pepperoni", "Cuatro quesos", "A la piedra"]
pizzas_amigo = ["Pepperoni", "Cuatro quesos", "A la piedra"]
pizzas.append("Americana")
pizzas_amigo.append("Hawaiana")
print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(f"- {pizza}")
print("\nLas pizzas favoritas de mi amigo son:")
for pizza in pizzas_amigo:
    print(f"- {pizza}")