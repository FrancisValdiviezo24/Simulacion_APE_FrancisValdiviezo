class CalcularTemperatura:
    def calcular(self, temperatura):
        if temperatura <= 10:
            return 1.0
        if temperatura >= 28:
            return 0.1
        return 1.0 - ((temperatura - 10) / 2) * 0.1
