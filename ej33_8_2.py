import json
from pathlib import Path
ruta_numero_favorito = Path("numero_favorito.json")
contenido = ruta_numero_favorito.read_text()
numero_leido = json.loads(contenido)
print(f"¡Sé cuál es tu número favorito! Es {numero_leido}.")