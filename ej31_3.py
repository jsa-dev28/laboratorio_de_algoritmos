import random
intentos = 0
ticket_ganador = []
loteria = [26, 17, 42, 8, 15, 4, 23, 9, 31, 12, "R", "B", "G", "O", "P"]
print("Cualquier boleto con los siguientes números o letras gana un premio:")
for i in range(4):
    print(random.choice(loteria))
ticket_ganador.append(random.choice(loteria))

while True:
    my_ticket = []
    for i in range(4):
        my_ticket.append(random.choice(loteria))

    print("Mi boleto:")
    for item in my_ticket:
        print(item)
    if my_ticket[0] in ticket_ganador and my_ticket[1] in ticket_ganador and my_ticket[2] in ticket_ganador and my_ticket[3] in ticket_ganador:
        print(f"¡Ganaste un premio! Tomó {intentos} intentos.")
        break
    else:
        print("No ganaste esta vez. Intentalo de nuevo.")
        intentos += 1
        print(f"Intentos: {intentos}")