import numpy as np

class Estocastico(Simulacion):

    @abstractMethod
    def modelo( self, p0, r, sigma, time):
        poblacion = []

        poblacion.append(p0)

        for t in time:
            ruido = np.randow.normal(loc=media, scale=sigma, size=0)
            