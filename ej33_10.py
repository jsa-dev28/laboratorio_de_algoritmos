from pathlib import Path
import json

def obtener_usuario_guardado(path):
    """Obtiene el nombre del usuario guardado si está disponible."""
    if path.exists():
        contenido = path.read_text()
        username = json.loads(contenido)
        return username
    else:
        return None

def obtener_nuevo_usuario(path):
    """Pide un nuevo nombre de usuario."""
    username= input("¿Cómo te llamás? ")
    edad = input("¿Cuántos años tenés? ")
    ciudad = input("¿En qué ciudad vivís? ")
    usuario = {
        "nombre": username,
        "edad": edad,
        "ciudad": ciudad
    }
    contenido = json.dumps(usuario)
    path.write_text(contenido)
    return username

def saludar_usuario():
    """Saluda a la persona usuaria por su nombre."""
    path = Path('username.json')
    username= obtener_usuario_guardado(path)
    if username:
        print(f"¡Bienvenido de nuevo, {username['nombre']}! Recordamos tus datos, tenés {username['edad']} años y vivís en {username['ciudad']}.")
    else:
        username= obtener_nuevo_usuario(path)
        print(f"Te vamos a recordar cuando vuelvas, {username}.")

saludar_usuario()
