import numpy as np


def modelo_estocastico(p0, tasa, sigma, periodos):
    tiempo = list(range(periodos + 1))
    poblacion = [p0]

    for periodo in range(periodos):
        poblacion_actual = poblacion[-1]
        ruido = np.random.normal(0, sigma)
        nueva_poblacion = poblacion_actual + tasa * poblacion_actual + ruido

        if nueva_poblacion < 0:
            nueva_poblacion = 0

        poblacion.append(nueva_poblacion)

    return tiempo, poblacion
