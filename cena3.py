personas = ["niki", "marangoni", "epstein"]
no_puede_ir = "epstein"
nuevo_invitado = "dantsteam"
personas.append(nuevo_invitado)
personas.remove(no_puede_ir)
print(f"El invitado {no_puede_ir} no puede ir a la cena, está muerto. Va a ir {nuevo_invitado} en su lugar")
print("Tengo una mesa más grande, así que puedo invitar a más personas")
personas.insert(0, "messi")
personas.insert(1, "cristiano")
for persona in personas:
    print(f"hola {persona}, te invito a mi cena")
print("Perdón, mi mesa no va a llegar a tiempo, solo puedo invitar a dos personas")
while len(personas) > 2:
    persona_eliminada = personas.pop()
    print(f"Perdon {persona_eliminada}, no puedo invitarte a la cena")
for persona in personas:
    print(f"Hola {persona}, todavía estás invitado a la cena")