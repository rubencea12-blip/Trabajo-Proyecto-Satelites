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
if __name__ == "__main__":
    iss = Satelite("ISS (ZARYA)", -41.0, -71.0, 419.7)
    print(iss)
    print(iss.tipo_orbita())
    print(iss.esta_en_zona((-76.30, -46.13, -66.30, -36.13)))
    print(Satelite("X", 0, 0, 35786).tipo_orbita())