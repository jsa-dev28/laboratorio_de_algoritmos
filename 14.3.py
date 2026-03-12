usuarios_acutales = ["juanjo", "maria", "pedro", "rosa", "luis"]
nuevos_usuarios = ["nestor", "Maria", "pedro", "ana", "carlos"]
nuevos_usuarios = [usuario.lower() for usuario in nuevos_usuarios]
usuarios_acutales = [usuario.lower() for usuario in usuarios_acutales]
for usuario in nuevos_usuarios:
    if usuario in usuarios_acutales:
        print(f"El nombre de usuario '{usuario}' no está disponible. Por favor, elige otro.")
    else:
        print(f"El nombre de usuario '{usuario}' está disponible.")