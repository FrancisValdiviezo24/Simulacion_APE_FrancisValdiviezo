import numpy as np


def modelo_deterministico(p0, tasa, periodos):
    tiempo = np.arange(0, periodos + 1)
    poblacion = p0 * np.exp(tasa * tiempo)
    return tiempo, poblacion
