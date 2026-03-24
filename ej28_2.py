class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad, intentos_login=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.intentos_login = intentos_login

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre}!")

    def incrementar_intentos_login(self):
        self.intentos_login += 1

    def reiniciar_intentos_login(self):
        self.intentos_login = 0
    
usuario1 = Usuario("Juanjo", "Shlamovitz", 16, "Buenos Aires")
usuario1.incrementar_intentos_login()   
usuario1.incrementar_intentos_login()
usuario1.incrementar_intentos_login()
print(f"Intentos de login: {usuario1.intentos_login}")
usuario1.reiniciar_intentos_login()
print(f"Intentos de login después de reiniciar: {usuario1.intentos_login}")
