from time import sleep
pedidos_sandwiches = ["atún", "pollo", "jamón y queso", "pastrón", "pastrón", "pastrón"]
sandwiches_terminados = []
print("Nos quedamos sin pastrón.")
while "pastrón" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastrón")
while pedidos_sandwiches:
    pedido = pedidos_sandwiches.pop(0)
    print(f"Preparé tu sándwich de {pedido}.")
    sandwiches_terminados.append(pedido)
    sleep(1)
print("Todos los sándwiches están listos. Los sándwiches preparados son:")
for sandwich in sandwiches_terminados:
    print(f"- {sandwich}")