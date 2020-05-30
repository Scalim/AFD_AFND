# Clase AFND

from servicio.automatafinito import AutomataFinito

class Afnd(AutomataFinito):
    def __init__(self, K, S, s, F, d):
        AutomataFinito.__init__(self, K, S, s, F, d)