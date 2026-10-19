def modelo_discreto(p0, tasa, periodos):
    tiempo = list(range(periodos + 1))
    poblacion = [p0]

    for periodo in range(periodos):
        poblacion_actual = poblacion[-1]
        nueva_poblacion = poblacion_actual + tasa * poblacion_actual
        poblacion.append(nueva_poblacion)

    return tiempo, poblacion
