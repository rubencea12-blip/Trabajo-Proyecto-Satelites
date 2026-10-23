import json

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


def leer_satelites(ruta):
    """Lee el json (utf-8) y devuelve la lista de registros."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("no se encontró el archivo:", ruta)
        return []


def contar_por_grupo(registros):
    """Devuelve {grupo: cantidad} con los satelites de cada grupo."""
    conteo = {}
    for registro in registros:
        nombre_grupo = grupo(registro["OBJECT_NAME"])
        if nombre_grupo in conteo:
            conteo[nombre_grupo] += 1
        else:
            conteo[nombre_grupo] = 1
    return conteo


def lanzamientos_por_anio(registros):
    """Devuelve {año: cantidad de satelites lanzados ese año}."""
    conteo = {}
    for registro in registros:
        anio = anio_lanzamiento(registro)
        if anio in conteo:
            conteo[anio] += 1
        else:
            conteo[anio] = 1
    return conteo


if __name__ == "__main__":
    print(anio_lanzamiento({"OBJECT_ID": "1998-067A"}))
    print(grupo("STARLINK-1234"))
    print(grupo("ISS (ZARYA)"))

    registros = leer_satelites("datos/satelites.json")
    print(len(registros))
    print(contar_por_grupo(registros))