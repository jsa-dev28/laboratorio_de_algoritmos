def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones is not None:
        album['canciones'] = canciones
    return album
print(hacer_album('Callejeros', 'Rocanroles sin destino'))
print(hacer_album('Los Piojos', '3er Arco'))
print(hacer_album('La Renga', 'Despedazado en mil partes', canciones=11))