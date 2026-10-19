from modelos.resultado import Resultado
from controlador.normalizar import Normalizar
from controlador.calcular_temperatura import CalcularTemperatura
from controlador.calcular_indice import CalcularIndice
from controlador.clasificacion import Clasificar


class Procesamiento:
    def procesar(self, datos, modelo):
        resultados = []
        normalizar = Normalizar()
        temperatura = CalcularTemperatura()
        calcular = CalcularIndice()
        clasificar = Clasificar()

        for clima in datos:
            h = normalizar.humedad(clima.humedad)
            n = normalizar.nubosidad(clima.nubosidad)
            tf = temperatura.calcular(clima.temperatura)

            if modelo == "base":
                indice = calcular.base(h, n, tf)
            else:
                indice = calcular.ajustado(h, n, tf)

            estado = clasificar.clasificar(indice)
            resultado = Resultado(clima.hora, clima.humedad, clima.nubosidad, clima.temperatura, h, n, tf, indice, estado)
            resultados.append(resultado)

        return resultados
