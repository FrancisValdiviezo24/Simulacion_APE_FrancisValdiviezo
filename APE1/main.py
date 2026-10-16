from models.clima import Clima
from controlador.calcular_indice import CalcularIndice
from controlador.calcular_temperatura import CalcularTemperatura
from controlador.clasificacion import Clasificar
from controlador.normalizar import Normalizar
from controlador.procesamiento import Procesamiento
from vista.climaVista import ClimaVista

def main():
    datos = [
        Clima("06:00", 65, 40, 14),
        Clima("08:00", 70, 50, 16),
        Clima("10:00", 68, 45, 18),
        Clima("12:00", 60, 30, 22),
        Clima("14:00", 75, 70, 20),
        Clima("16:00", 85, 85, 18),
        Clima("18:00", 92, 95, 16),
        Clima("20:00", 88, 90, 17),
        Clima("22:00", 80, 75, 15)
    ]

    controlador = Procesamiento()
    vista = ClimaVista()

    resultados = controlador.procesarDatos(datos)

    vista.mostrarTabla(resultados)
    vista.mostrarGrafica(resultados)

if __name__ == "__main__":
    main()