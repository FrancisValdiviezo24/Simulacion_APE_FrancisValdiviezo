class CalcularIndice:
    def base(self, h, n, tf):
        return 0.5 * h + 0.3 * n + 0.2 * tf

    def ajustado(self, h, n, tf):
        return 0.45 * h + 0.4 * n + 0.15 * tf
