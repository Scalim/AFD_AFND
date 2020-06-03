class AutomataFinito:
    def __init__(self, K, E, S, F, s):
        self.K = K  # (Σ) Alfabeto
        self.E = E  # (K) Nodos
        self.S = S  # (S) Iniciales
        self.F = F  # (F) Finales
        self.s = s  # (δ) Conexiones

    def nodosString():
        return "K = {" + ", ".join(self.K) + "}"

    def alfabetoString():
        return "Σ = {" + ", ".join(self.E) + "}"

    def inicialesString():
        return "S = {" + ", ".join(self.S) + "}"

    def finalesString(self):
        return "F = {" + ", ".join(self.F) + "}"

    def conexionesString(self):
        return "δ = {" + ", ".join(self.s) + "}"

    def mostrarQuintupla(self):
        print(self.nodosString())
        print(self.alfabetoString())
        print(self.inicialesString())
        print(self.finalesString())
        print(self.conexionesString())

    def esAfnd(self):
        for conexion in self.s:
            if (conexion[1] == None)
            # Si la letra de esa arista es vacío
            return True
        return False

    def obtenerAfd(self):
        if (self.esAfnd()):
            # Lógica de conversión
        else:
            return self

    def simplificarAfd(self):
        # Lógica de simplificación

    def operar(self, operacion, automata):
        if (operacion == "complemento"):
            # Lógica del complemento
        elif (operacion == "interseccion"):
            # Lógica de la intersección
        elif (operacion == "union"):
            # Lógica de la unión
        elif (operacion == "concatenacion"):
            # Lógica de la concatenación
