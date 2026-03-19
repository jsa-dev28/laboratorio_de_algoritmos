def hacer_auto(fabricante, modelo, **caracteristicas):
    auto = {'fabricante': fabricante, 'modelo': modelo}
    for clave, valor in caracteristicas.items():
        auto[clave] = valor
    return auto
auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)
print(auto)