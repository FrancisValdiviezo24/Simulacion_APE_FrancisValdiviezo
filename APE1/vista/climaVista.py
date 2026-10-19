import matplotlib.pyplot as plt


class ClimaVista:
    def mostrar_tabla(self, titulo, resultados):
        print("\n" + titulo)
        print(f"{'Hora':<7}{'Hum':<7}{'Nub':<7}{'Temp':<7}{'H':<7}{'N':<7}{'Tf':<7}{'Índice':<9}{'Estado'}")
        print("-" * 78)

        for r in resultados:
            print(f"{r.hora:<7}{r.humedad:<7}{r.nubosidad:<7}{r.temperatura:<7}{r.h:<7.2f}{r.n:<7.2f}{r.tf:<7.2f}{r.indice:<9.3f}{r.estado}")

    def guardar_grafica(self, resultados_base, resultados_ajustados):
        horas = []
        indices_base = []
        indices_ajustados = []

        for resultado in resultados_base:
            horas.append(resultado.hora)
            indices_base.append(resultado.indice)

        for resultado in resultados_ajustados:
            indices_ajustados.append(resultado.indice)

        plt.plot(horas, indices_base, marker="o", label="Modelo base")
        plt.plot(horas, indices_ajustados, marker="o", label="Modelo ajustado")
        plt.axhline(0.75, color="red", linestyle="--", label="Lluvia")
        plt.title("Índice de posibilidad de lluvia")
        plt.xlabel("Hora")
        plt.ylabel("Índice")
        plt.ylim(0, 1)
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig("grafica_lluvia.png")
        plt.close()
