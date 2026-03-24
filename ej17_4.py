buenos_aires = {
    "Población": 2890000,
    "País": "Argentina",
    "Dato curioso": "Es conocida como la 'Ciudad de la Furia'."
}

madrid = {
    "Población": 3223000,
    "País": "España",
    "Dato curioso": "Es famosa por su vida nocturna y su arte."
}

londres = {
    "Población": 8982000,
    "País": "Reino Unido",
    "Dato curioso": "Es el hogar del Big Ben y el Palacio de Buckingham."
}

ciudades = {
    "Buenos Aires": buenos_aires,
    "Madrid": madrid,
    "Londres": londres,
}

for ciudad, info in ciudades.items():
    print(f"\nCiudad: {ciudad}")
    print(f"País: {info['País']}")
    print(f"Población: {info['Población']}")
    print(f"Dato curioso: {info['Dato curioso']}")
