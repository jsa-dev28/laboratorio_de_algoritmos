class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina, clientes_atendidos=0):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = clientes_atendidos

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")

    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad

restaurante = Restaurante("La Buena Mesa", "italiana")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()
print(f"Clientes atendidos: {restaurante.clientes_atendidos}")
restaurante.establecer_clientes_atendidos(50)
print(f"Clientes atendidos después de establecer: {restaurante.clientes_atendidos}")
restaurante.incrementar_clientes_atendidos(20)
print(f"Clientes atendidos después de incrementar: {restaurante.clientes_atendidos}")