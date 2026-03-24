from ej30_3_1 import Usuario
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