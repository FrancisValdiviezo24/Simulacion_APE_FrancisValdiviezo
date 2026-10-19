from modelos.clima import Clima
from controlador.procesamiento import Procesamiento
from vista.climaVista import ClimaVista


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

procesamiento = Procesamiento()
vista = ClimaVista()
resultados_base = procesamiento.procesar(datos, "base")
resultados_ajustados = procesamiento.procesar(datos, "ajustado")

vista.mostrar_tabla("MODELO BASE", resultados_base)
vista.mostrar_tabla("MODELO AJUSTADO", resultados_ajustados)
vista.guardar_grafica(resultados_base, resultados_ajustados)

print("\nGráfica guardada en grafica_lluvia.png")
