import random
loteria = [26, 17, 42, 8, 15, 4, 23, 9, 31, 12, "R", "B", "G", "O", "P"]
print("Cualquier boleto con los siguientes números o letras gana un premio:")
for i in range(4):
    print(random.choice(loteria))
