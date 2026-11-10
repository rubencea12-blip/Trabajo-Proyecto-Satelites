import matplotlib.pyplot as plt
import numpy as np


def barras_lanzamientos(lanzamientos, archivo):
    """Barras con la cantidad de satelites lanzados por año."""
    anios = sorted(lanzamientos)
    cantidades = []
    for anio in anios:
        cantidades.append(lanzamientos[anio])
    plt.figure(figsize=(10, 5))
    plt.bar(anios, cantidades)
    plt.title("Satélites lanzados por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de satélites")
    plt.savefig("salidas/" + archivo)
    plt.show()


def barras_apiladas(lanzamientos_a, lanzamientos_b, etiqueta_a, etiqueta_b, archivo):
    """Barras apiladas de dos series {año: cantidad}."""
    anios = sorted(set(lanzamientos_a) | set(lanzamientos_b))
    valores_a = []
    valores_b = []
    for anio in anios:
        valores_a.append(lanzamientos_a.get(anio, 0))
        valores_b.append(lanzamientos_b.get(anio, 0))
    plt.figure(figsize=(10, 5))
    plt.bar(anios, valores_a, label=etiqueta_a)
    plt.bar(anios, valores_b, bottom=valores_a, label=etiqueta_b)
    plt.title("Lanzamientos por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de satélites")
    plt.legend()
    plt.savefig("salidas/" + archivo)
    plt.show()
    
def barras_altura_media(resumen, archivo):
    """Barras con la altitud media de cada grupo."""
    grupos = list(resumen.keys())
    medias = []
    for nombre_grupo in grupos:
        medias.append(resumen[nombre_grupo]["media"])
    plt.figure(figsize=(10, 5))
    plt.bar(grupos, medias)
    plt.title("Altitud media por grupo")
    plt.xlabel("Grupo")
    plt.ylabel("Altitud media (km)")
    plt.savefig("salidas/" + archivo)
    plt.show()

def histograma_altitudes_leo(satelites, archivo, ancho_bin=10):
    """Histograma de altitudes entre 200 y 2000 km."""
    altitudes = []
    for satelite in satelites:
        if 200 <= satelite.altitud_km <= 2000:
            altitudes.append(satelite.altitud_km)
    plt.figure(figsize=(10, 5))
    plt.hist(altitudes, bins=np.arange(200, 2000 + ancho_bin, ancho_bin))
    plt.title("Altitudes en órbita baja")
    plt.xlabel("Altitud (km)")
    plt.ylabel("Cantidad de satélites")
    plt.savefig("salidas/" + archivo)
    plt.show()


def histograma_altitudes_log(satelites, archivo, n_bins=60):
    """Histograma de todas las altitudes con eje X logaritmico."""
    altitudes = []
    for satelite in satelites:
        altitudes.append(satelite.altitud_km)
    bins = np.logspace(np.log10(min(altitudes)), np.log10(max(altitudes)), n_bins)
    plt.figure(figsize=(10, 5))
    plt.hist(altitudes, bins=bins)
    plt.xscale("log")
    plt.title("Altitudes de todos los satélites")
    plt.xlabel("Altitud (km, escala logarítmica)")
    plt.ylabel("Cantidad de satélites")
    plt.savefig("salidas/" + archivo)
    plt.show()

def histograma_inclinaciones(registros, archivo):
    """Histograma de la inclinacion de las orbitas, de 0 a 180 grados."""
    inclinaciones = []
    for registro in registros:
        inclinaciones.append(registro["INCLINATION"])
    plt.figure(figsize=(10, 5))
    plt.hist(inclinaciones, bins=np.arange(0, 181, 1))
    plt.title("Inclinaciones de las órbitas")
    plt.xlabel("Inclinación (grados)")
    plt.ylabel("Cantidad de satélites")
    plt.savefig("salidas/" + archivo)
    plt.show()


def dispersion_posiciones(satelites, archivo):
    """Grafico de puntos con la longitud y la latitud de cada satelite."""
    longitudes = []
    latitudes = []
    for satelite in satelites:
        longitudes.append(satelite.longitud)
        latitudes.append(satelite.latitud)
    plt.figure(figsize=(12, 6))
    plt.plot(longitudes, latitudes, ".", markersize=1)
    plt.title("Posición de los satélites")
    plt.xlabel("Longitud (grados)")
    plt.ylabel("Latitud (grados)")
    plt.savefig("salidas/" + archivo)
    plt.show()   