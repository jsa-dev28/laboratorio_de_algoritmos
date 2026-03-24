from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
fecha_nacimiento = input("Ingrese su fecha de nacimiento (ddmmyyyy): ")
if fecha_nacimiento in pi_string:
    print("¡Tu fecha de nacimiento está en el primer millón de dígitos de pi!")
else:
    print("Tu fecha de nacimiento no está en el primer millón de dígitos de pi.")