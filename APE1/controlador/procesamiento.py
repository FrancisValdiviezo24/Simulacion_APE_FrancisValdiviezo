class Procesamiento:
    def procesar (self,clima):
        h = self.normalizarHumedad(clima.humedad)
    
        n = self.normalizarNubosidad(clima.nubosidad)

        tf = self.calcularFT(clima.temperatura)

        indice = self.calcular_indice_base (h,n,tf)

        estado = self.clasifcar(indice)

        return Resultado(clima.hora, clima.humedad, clima.nubosidad, clima.temperatua,h,n,tf,indice, estado)


    def procesarDatos (self, datos):
        resultados = []

        for clima in datos:
            resultado = self.procesar(clima)
            resultados.append(resultado)

        return resultados