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

## Etapa 1

1. Carga de datos
2. Grupos
3. Lanzamientos por año
4. Tipos de órbita
5. Extremos
6. Comparación de grupos
7. Satélites sobre Bariloche
8. Conclusiones

## Etapa 2

1. Lanzamientos por año, con barras apiladas de Starlink contra el resto
2. Altura media por grupo
3. Altitudes en órbita baja (bins de 10 y de 50 km)
4. Todas las altitudes en escala logarítmica
5. Inclinaciones, con filtro por grupo