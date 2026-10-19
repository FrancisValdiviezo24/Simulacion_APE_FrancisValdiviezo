import matplotlib.pyplot as plt
from controller.deterministico import modelo_deterministico


class SimulacionVista:
    def mostrar_tabla(self, datos, resultado, tasa, sigma, paso):
        print(f"Tasa de crecimiento: {tasa}")
        print(f"Nivel de ruido: {sigma}")
        print(f"Paso de Euler: {paso}\n")
        print(f"{'Tiempo':<9}{'Datos':<12}{'Determin.':<14}{'Discreto':<14}{'Estocástico':<15}{'Continuo'}")
        print("-" * 78)

        for i in range(len(datos)):
            print(f"{i:<9}{datos[i]:<12.2f}{resultado.deterministico[i]:<14.2f}{resultado.discreto[i]:<14.2f}{resultado.estocastico[i]:<15.2f}{resultado.continuo_entero[i]:.2f}")

    def guardar_comparacion(self, datos, resultado):
        plt.plot(resultado.tiempo, datos, "ko--", label="Datos de entrada")
        plt.plot(resultado.tiempo, resultado.deterministico, marker="o", label="Determinístico")
        plt.plot(resultado.tiempo_discreto, resultado.discreto, marker="s", label="Discreto")
        plt.plot(resultado.tiempo_estocastico, resultado.estocastico, marker="^", label="Estocástico")
        plt.plot(resultado.tiempo_continuo, resultado.continuo, label="Continuo")
        plt.title("Comparación de modelos de crecimiento poblacional")
        plt.xlabel("Tiempo")
        plt.ylabel("Población")
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig("comparacion_modelos.png")
        plt.close()

    def guardar_influencia_tasa(self, poblacion_inicial, periodos):
        for tasa in [-0.12, 0, 0.12]:
            tiempo, poblacion = modelo_deterministico(poblacion_inicial, tasa, periodos)
            plt.plot(tiempo, poblacion, marker="o", label=f"r = {tasa}")

        plt.title("Influencia de la tasa de crecimiento")
        plt.xlabel("Tiempo")
        plt.ylabel("Población")
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig("influencia_tasa.png")
        plt.close()
