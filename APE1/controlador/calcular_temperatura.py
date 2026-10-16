
class CalcularTemperatura:
    def calcularFT (self, temperatura):
        if temperatura <= 10:
            return 1

        if temperatura >= 28:
            return 0.10

        if temperatura > 10 and temperatura < 28:
            v_inicial = 10
            factor = 1.0

            while v_inicial <= temmperatura:

                if valor % 2 == 0:
                    return factor - 0.10

                v_inicial += 1
