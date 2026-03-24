from random import randint
def generar_cumpleaños(n):
    cumpleaños = []
    for _ in range(n):
        día = randint(1, 31)
        mes = randint(1, 12)
        cumpleaños.append((día, mes))
    return cumpleaños
def tiene_cumpleaños_repetido(cumpleaños):
    return len(cumpleaños) != len(set(cumpleaños))
def probar_paradoja(n, experimentos):
    coincidencias = 0
    for _ in range(experimentos):
        cumpleaños = generar_cumpleaños(n)
        if tiene_cumpleaños_repetido(cumpleaños):
            coincidencias += 1
    probabilidad = coincidencias / experimentos
    print(f"Para {n} personas, la probabilidad de que al menos dos compartan cumpleaños es: {probabilidad * 100}%")
for n in range(5, 101, 5):
    probar_paradoja(n, 10000)
