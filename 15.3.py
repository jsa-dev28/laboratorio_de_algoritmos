#mejorá el código del ejercicio 15.3 reemplazando la serie de llamadas a print() por un loop que pase por todas las claves y valores del diccionario. Cuando estés seguro de que el loop funciona, agregá cinco términos más de Python a tu glosario. Cuando vuelvas a ejecutar el programa, estas nuevas palabras y sus significados deberían aparecer automáticamente en la salida.
glosario = {
    "string" : "cadena de caracteres",
    "integer": "número entero",
    "input": "entrada de datos",
    "if": "si",
    "else": "sino",
    }
for termino, significado in glosario.items():
    print(f"{termino}: {significado}")