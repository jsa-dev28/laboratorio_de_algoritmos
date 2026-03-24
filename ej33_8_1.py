import json
from pathlib import Path
ruta_numero_favorito = Path("numero_favorito.json")
numero_favorito = input("¿Cuál es tu número favorito? ")
contenido = json.dumps(numero_favorito)
ruta_numero_favorito.write_text(contenido)
