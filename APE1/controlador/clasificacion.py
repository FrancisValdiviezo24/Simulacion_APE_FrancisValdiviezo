
class Clasificar:
    def clasifcar (self, indice):
        if indice < 0.40:
            resp = "Sin Lluvia"
            return resp
        elif indice < 0.60:
            resp = "Baja Posibilidad"
            return resp
        elif indice < 0.75:
            resp = "Lluvia Propable"
            return resp
        else :
            resp = "Lluvia"
            return resp