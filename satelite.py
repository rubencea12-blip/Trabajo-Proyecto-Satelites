from funciones_base import crear_objeto_skyfield, obtener_posicion


class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los datos del satelite."""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

    def tipo_orbita(self):
        """Devuelve el tipo de orbita segun la altitud."""
        if self.altitud_km < 2000:
            return "LEO"
        elif self.altitud_km < 34000:
            return "MEO"
        elif self.altitud_km <= 37000:
            return "GEO"
        else:
            return "HEO"

    def esta_en_zona(self, zona):
        """Dice si el satelite esta dentro de la zona."""
        lon_min, lat_min, lon_max, lat_max = zona
        if lon_min <= self.longitud <= lon_max:
            if lat_min <= self.latitud <= lat_max:
                return True
        return False

    def __str__(self):
        """Devuelve el satelite como texto."""
        return f"{self.nombre} | {self.tipo_orbita()} | {self.altitud_km:.1f} km"


def crear_satelites(registros, momento):
    """Devuelve una lista de Satelite con su posicion en momento."""
    satelites = []
    for registro in registros:
        objeto = crear_objeto_skyfield(registro)
        latitud, longitud, altitud = obtener_posicion(objeto, momento)
        if altitud >= 100:
            satelites.append(Satelite(registro["OBJECT_NAME"],
                                      latitud, longitud, altitud))
    return satelites


if __name__ == "__main__":
    from datetime import datetime, timezone
    from catalogo import leer_satelites

    iss = Satelite("ISS (ZARYA)", -41.0, -71.0, 419.7)
    print(iss)
    print(iss.tipo_orbita())
    print(iss.esta_en_zona((-76.30, -46.13, -66.30, -36.13)))
    print(Satelite("X", 0, 0, 35786).tipo_orbita())

    registros = leer_satelites("datos/satelites.json")
    ahora = datetime.now(timezone.utc)
    satelites = crear_satelites(registros[:100], ahora)
    print(len(satelites))
    print(satelites[0])