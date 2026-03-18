messi = {
    "nombre": "Lionel",
    "apellido": "Messi",
    "edad": 38,
    "ciudad en la que vive": "Miami",
}
cristiano = {
    "nombre": "Cristiano",
    "apellido": "Ronaldo",
    "edad": 41,
    "ciudad en la que vive": "Riad",
}
di_maria = {
    "nombre": "Ángel",
    "apellido": "Di María",
    "edad": 38,
    "ciudad en la que vive": "Rosario",
}

gente = [messi, cristiano, di_maria]
for persona in gente:
    print(f"\nNombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"Edad: {persona['edad']}")
    print(f"Ciudad en la que vive: {persona['ciudad en la que vive']}")