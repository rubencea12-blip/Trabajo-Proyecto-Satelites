def contar_por_tipo(satelites):
    """Devuelve cuantos satelites hay de cada tipo de orbita."""
    conteo = {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
    for satelite in satelites:
        conteo[satelite.tipo_orbita()] += 1
    return conteo


def mas_bajo(satelites):
    """Devuelve el satelite de menor altitud."""
    bajo = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km < bajo.altitud_km:
            bajo = satelite
    return bajo


def mas_alto(satelites):
    """Devuelve el satelite de mayor altitud."""
    alto = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km > alto.altitud_km:
            alto = satelite
    return alto


if __name__ == "__main__":
    from satelite import Satelite
    lista = [Satelite("A", 0, 0, 500), Satelite("B", 0, 0, 35786), Satelite("C", 0, 0, 20000)]
    print(contar_por_tipo(lista))
    print(mas_bajo(lista))
    print(mas_alto(lista))