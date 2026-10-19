import numpy as np


def modelo_continuo(p0, tasa, periodos, paso):
    tiempo = np.arange(0, periodos + paso, paso)
    poblacion = [p0]

    for instante in tiempo[1:]:
        poblacion_actual = poblacion[-1]
        cambio = tasa * poblacion_actual
        nueva_poblacion = poblacion_actual + paso * cambio
        poblacion.append(nueva_poblacion)

    return tiempo, poblacion
