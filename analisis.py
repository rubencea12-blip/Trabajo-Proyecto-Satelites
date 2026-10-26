from catalogo import grupo


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


def en_zona(satelites, zona):
    """Devuelve los satelites que estan dentro de la zona."""
    resultado = []
    for satelite in satelites:
        if satelite.esta_en_zona(zona):
            resultado.append(satelite)
    return resultado


def ordenar_por(satelites, atributo, descendente=False):
    """Devuelve una lista nueva ordenada por el atributo indicado."""
    return sorted(satelites, key=lambda s: getattr(s, atributo),
                  reverse=descendente)


def top_n(satelites, n, mas_altos=True):
    """Devuelve los n satelites mas altos (o mas bajos)."""
    ordenados = ordenar_por(satelites, "altitud_km", descendente=mas_altos)
    return ordenados[:n]


def resumen_por_grupo(satelites):
    """Devuelve minima, media y maxima de altitud de cada grupo."""
    altitudes = {}
    for satelite in satelites:
        nombre_grupo = grupo(satelite.nombre)
        if nombre_grupo not in altitudes:
            altitudes[nombre_grupo] = []
        altitudes[nombre_grupo].append(satelite.altitud_km)

    resumen = {}
    for nombre_grupo, lista in altitudes.items():
        resumen[nombre_grupo] = {
            "cantidad": len(lista),
            "minima": min(lista),
            "media": sum(lista) / len(lista),
            "maxima": max(lista),
        }
    return resumen


if __name__ == "__main__":
    from satelite import Satelite
    lista = [
        Satelite("STARLINK-1", -40.0, -70.0, 550),
        Satelite("STARLINK-2", 10.0, 20.0, 560),
        Satelite("ISS", 0.0, 0.0, 420),
        Satelite("GPS", -41.0, -71.0, 20000),
    ]
    zona = (-76.30, -46.13, -66.30, -36.13)
    print([s.nombre for s in en_zona(lista, zona)])
    print([s.nombre for s in ordenar_por(lista, "altitud_km")])
    print([s.nombre for s in top_n(lista, 2)])
    print(resumen_por_grupo(lista))