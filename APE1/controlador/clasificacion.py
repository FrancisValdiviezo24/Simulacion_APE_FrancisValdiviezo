class Clasificar:
    def clasificar(self, indice):
        if indice < 0.40:
            return "Sin lluvia"
        if indice < 0.60:
            return "Baja posibilidad"
        if indice < 0.75:
            return "Lluvia probable"
        return "Lluvia"
