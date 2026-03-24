import json
from pathlib import Path
ruta_numero_favorito = Path("numero_favorito.json")
if ruta_numero_favorito.exists():
    contenido = ruta_numero_favorito.read_text()
    numero_leido = json.loads(contenido)
    print(f"¡Sé cuál es tu número favorito! Es {numero_leido}.")
else:
    numero_favorito = input("¿Cuál es tu número favorito? ")
    contenido = json.dumps(numero_favorito)
    ruta_numero_favorito.write_text(contenido)
    print(f"¡Sé cuál es tu número favorito! Es {numero_favorito}.")