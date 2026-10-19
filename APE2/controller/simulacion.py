import numpy as np
from controller.deterministico import modelo_deterministico
from controller.discreto import modelo_discreto
from controller.estocastico import modelo_estocastico
from controller.continuo import modelo_continuo
from models.resultado import Resultado


class Simulacion:
    def __init__(self, datos, tasa, sigma, paso):
        self.datos = datos
        self.tasa = tasa
        self.sigma = sigma
        self.paso = paso

    def ejecutar(self):
        poblacion_inicial = self.datos[0]
        periodos = len(self.datos) - 1

        np.random.seed(10)

        tiempo, deterministico = modelo_deterministico(poblacion_inicial, self.tasa, periodos)
        tiempo_discreto, discreto = modelo_discreto(poblacion_inicial, self.tasa, periodos)
        tiempo_estocastico, estocastico = modelo_estocastico(poblacion_inicial, self.tasa, self.sigma, periodos)
        tiempo_continuo, continuo = modelo_continuo(poblacion_inicial, self.tasa, periodos, self.paso)

        continuo_entero = []
        for periodo in tiempo:
            posicion = int(periodo / self.paso)
            continuo_entero.append(continuo[posicion])

        return Resultado(
            tiempo,
            deterministico,
            tiempo_discreto,
            discreto,
            tiempo_estocastico,
            estocastico,
            tiempo_continuo,
            continuo,
            continuo_entero
        )
