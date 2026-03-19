def construir_perfil(nombre, apellido, **info_usuario):
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario
perfil_usuario = construir_perfil('Juanjo', 'Shlamovitz', edad=16, ciudad='Buenos Aires', profesión='Estudiante')
print(perfil_usuario)