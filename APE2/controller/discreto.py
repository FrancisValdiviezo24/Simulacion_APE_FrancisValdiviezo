import numpy as np

class Discreto(Simulacion):

    @abstractMethod
    def modelo( self, p0, r, time):
        poblacion = []

        poblacion.append(p0)

        for t in time:
            ultimaPoblacion = poblacion [-1]

            incremento = r*ultimaPoblacion

            nuevaPoblacion = ultimaPoblacion + incremento 

            poblacion.append(nuevaPoblacion)

        return time, poblacion
