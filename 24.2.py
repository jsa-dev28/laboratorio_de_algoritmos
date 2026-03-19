def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop(0)
        print(mensaje)
        mensajes_enviados.append(mensaje)
mensajes = ['Hola', '¿Cómo estás?', '¡Hasta luego!']
mensajes_enviados = []
enviar_mensajes(mensajes, mensajes_enviados)
print("Mensajes:", mensajes)
print("Mensajes enviados:", mensajes_enviados)