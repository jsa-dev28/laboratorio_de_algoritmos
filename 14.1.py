usuarios = ["juanjo", "maria", "pedro", "admin"]
for usuario in usuarios:
    if usuario == "admin":
        print("¡Hola admin! ¿Querés ver un informe de estado?")
    else:
        print(f"¡Hola {usuario}! Gracias por iniciar sesión.")
