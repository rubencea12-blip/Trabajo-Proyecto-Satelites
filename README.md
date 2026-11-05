# Proyecto Satélites

Proyecto de Programación 1. Lee un catálogo de satélites en formato JSON, los agrupa y cuenta por grupo, año de lanzamiento y tipo de órbita, calcula su posición con Skyfield y muestra los resultados en un notebook con gráficos.

## Integrantes

- Ruben Cea: hice todo el proyecto (catálogo, clase Satelite, análisis, gráficos e informe).

## Cómo correr el proyecto

1. Crear el ambiente: `python -m venv .venv`
2. Activarlo: `.venv\Scripts\activate`
3. Instalar skyfield siguiendo la guía `instalacion.md`, y además: `pip install matplotlib numpy`
4. Abrir `informe.ipynb` y ejecutar todo

## Archivos

- `datos/satelites.json`: el catálogo de satélites
- `funciones_base.py`: funciones con Skyfield 
- `catalogo.py`: lectura del JSON, grupos y lanzamientos por año
- `satelite.py`: clase Satelite y crear_satelites
- `analisis.py`: conteos, extremos, ordenamiento y zonas
- `graficos.py`: gráficos de barras e histogramas
- `informe.ipynb`: el informe
- `salidas/`: figuras generadas por los gráficos