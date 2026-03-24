mascota1 = {
    "tipo de animal": "perro",
    "nombre del dueño": "Juan",
}
mascota2 = {
    "tipo de animal": "gato",
    "nombre del dueño": "Sara",
}
mascota3 = {
    "tipo de animal": "conejo",
    "nombre del dueño": "Eduardo",
}
mascotas = [mascota1, mascota2, mascota3]
for mascota in mascotas:
    print(f"\nTipo de animal: {mascota['tipo de animal']}")
    print(f"Nombre del dueño: {mascota['nombre del dueño']}")