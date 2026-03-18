lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas = ['Juan', 'Sara', 'Eduardo', 'Agustina', 'María', "Carlos"]
for persona in personas:
    if persona in lenguajes_favoritos:
        lenguaje = lenguajes_favoritos[persona].title()
        print(f"{persona}, gracias por responder tu lenguaje favorito: {lenguaje}.")
    else:
        print(f"{persona}, ¿cuál es tu lenguaje de programación favorito?")