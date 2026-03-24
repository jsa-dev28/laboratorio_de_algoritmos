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

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Los privilegios del administrador {self.nombre} son:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")

admin = Administrador("Carlos", "Martínez", 25, "Córdoba", ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"])
admin.mostrar_privilegios()