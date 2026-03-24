personas = ["niki", "marangoni", "ivo"]
no_puede_ir = "marangoni"
nuevo_invitado = "dantsteam"
personas.append(nuevo_invitado)
personas.remove(no_puede_ir)
print(f"El invitado {no_puede_ir} no puede ir a la cena. Va a ir {nuevo_invitado} en su lugar")
for persona in personas:
    print(f"hola {persona}, te invito a mi cena")