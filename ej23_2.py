def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones is not None:
        album['canciones'] = canciones
    return album
print(hacer_album('Los Redondos', 'La mosca y la sopa'))
print(hacer_album('Los Piojos', '3er Arco'))
print(hacer_album('La Renga', 'Despedazado por mil partes', canciones=11))