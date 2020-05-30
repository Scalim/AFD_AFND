# Clase AFD

from servicio.automatafinito import AutomataFinito

class Afd(AutomataFinito):
    def __init__(self, afnd):
        AutomataFinito.__init__(self, afnd.K, afnd.S, afnd.s, afnd.F, afnd.d)
        self.afndAAfd(afnd.tablaDeTransicion(), afnd.s, afnd.F)