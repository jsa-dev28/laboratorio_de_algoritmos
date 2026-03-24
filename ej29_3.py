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

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios
    def mostrar_privilegios(self):
        print(f"Los privilegios son:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad, ciudad)
        self.privilegios = Privilegios(["puede agregar post", "puede eliminar post", "puede banear usuario"])
        
admin = Administrador("Carlos", "Martínez", 25, "Córdoba")
admin.privilegios.mostrar_privilegios()
