class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Los sabores disponibles en {self.nombre_restaurante} son: {', '.join(self.sabores)}.")

puesto = PuestoDeHelados("Helados del Sol", "helados", ["dulce de leche", "chocolate", "frutilla"])
puesto.mostrar_sabores()