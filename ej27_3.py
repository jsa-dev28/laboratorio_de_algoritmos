class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")
    def saludar_usuario(self):
        print(f"Hola, {self.nombre}!")

usuario1 = Usuario("Juanjo", "Shlamovitz", 16, "Buenos Aires")
usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario2 = Usuario("Carlos", "Martinez", 25, "Córdoba")
usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario3 = Usuario("Martín", "González", 40, "Rosario")
usuario3.describir_usuario()
usuario3.saludar_usuario()