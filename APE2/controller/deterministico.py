import numpy as np
class Deterministico(Simulacion):

    @abstractMethod
    def modelo (self, p0, r, t):
        #t = np.arange(0, t +1)
        
        timpo = []

        for time in t:
            time = po * np.exp(r*time)
            tiempo.append(time)

        return time, tiempo