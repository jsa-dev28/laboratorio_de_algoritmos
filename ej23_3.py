def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones is not None:
        album['canciones'] = canciones
    return album
while True:
    print("Ingrese el nombre del artista (o 'salir' para terminar):")
    artista = input()
    if artista.lower() == 'salir':
        break
    print("Ingrese el título del álbum:")
    titulo = input()
    print("Ingrese la cantidad de canciones (opcional, presione Enter para omitir):")
    canciones_input = input()
    canciones = int(canciones_input) if canciones_input else None
    album_info = hacer_album(artista, titulo, canciones)
    print(album_info)