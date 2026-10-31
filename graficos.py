import matplotlib.pyplot as plt


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