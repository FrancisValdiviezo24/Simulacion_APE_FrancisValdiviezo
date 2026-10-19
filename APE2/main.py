from controller.simulacion import Simulacion
from vista.simulacion_vista import SimulacionVista


datos = [1000, 1100, 1250, 1400, 1600, 1850, 2100]
tasa = 0.12
sigma = 50
paso = 0.1

simulacion = Simulacion(datos, tasa, sigma, paso)
vista = SimulacionVista()
resultado = simulacion.ejecutar()

vista.mostrar_tabla(datos, resultado, tasa, sigma, paso)
vista.guardar_comparacion(datos, resultado)
vista.guardar_influencia_tasa(datos[0], len(datos) - 1)

print("\nGráficas guardadas en comparacion_modelos.png e influencia_tasa.png")
