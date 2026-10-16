import matplotlib.pyplot as plt

class ClimaVista:
    def mostrarTabla (self, resultados):
        print (
            f"{'Hora':<8}"
            f"{'Hum':<8}"
            f"{'Nub':<8}"
            f"{'Temp':<8}"
            f"{'H':<8}"
            f"{'N':<8}"
            f"{'Tf':<8}"
            f"{'Índice':<10}"
            f"{'Estado'}")

        print ("-" * 90)

        for r in resultados:
            print(
                f"{r.hora:<8}"
                f"{r.humedad:<8}"
                f"{r.nubosidad:<8}"
                f"{r.temperatura:<8}"
                f"{r.h:<8.2f}"
                f"{r.n:<8.2f}"
                f"{r.tf:<8.2f}"
                f"{r.indice:<10.3f}"
                f"{r.estado}"
            )
    
        def mostrarGrafica(self, resultados):

        horas = []
        indices = []

        for r in resultados:
            horas.append(r.hora)
            indices.append(r.indice)

        plt.plot(
            horas,
            indices,
            marker="o"
        )

        plt.title("Índice de posibilidad de lluvia")
        plt.xlabel("Hora")
        plt.ylabel("Índice")
        plt.grid()

        plt.show()