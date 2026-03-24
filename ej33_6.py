from pathlib import Path
ruta_gatos = Path("gatos.txt")
ruta_perros = Path("perros.txt")
archivos = [ruta_gatos, ruta_perros]
for archivo in archivos:
    try:
        contenido = archivo.read_text()
        print(f"\nContenido de {archivo.name}:")
        print(contenido)
    except FileNotFoundError:
        pass