GRUPOS = {
    "STARLINK": "Starlink",
    "ONEWEB": "OneWeb",
    "KUIPER": "Kuiper",
    "QIANFAN": "Qianfan",
    "IRIDIUM": "Iridium",
    "GLOBALSTAR": "Globalstar",
    "NAVSTAR": "GPS",
    "BEIDOU": "BeiDou",
}


def anio_lanzamiento(registro):
    """Devuelve el año de lanzamiento como int, segun OBJECT_ID."""
    return int(registro["OBJECT_ID"][:4])


def grupo(nombre):
    """Devuelve el grupo del satelite segun como empieza su nombre."""
    for prefijo in GRUPOS:
        if nombre.startswith(prefijo):
            return GRUPOS[prefijo]
    return "Otros"

if __name__ == "__main__":
    print(anio_lanzamiento({"OBJECT_ID": "1998-067A"}))
    print(grupo("STARLINK-1234"))
    print(grupo("ISS (ZARYA)"))