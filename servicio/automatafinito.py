class AutomataFinito:
    def __init__(self, K, E, S, F, s):
        self.K = K  # (Σ) Alfabeto
        self.E = E  # (K) Nodos
        self.S = S  # (S) Iniciales
        self.F = F  # (F) Finales
        self.s = s  # (δ) Conexiones

    def nodosString(self):
        return "K = {" + ", ".join(self.K) + "}"

    def alfabetoString(self):
        return "Σ = {" + ", ".join(self.E) + "}"

    def inicialesString(self):
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
            if (conexion[1] == None):
                # Si la letra de esa arista es vacío
                return True
        return False

    def obtenerAfd(self):
        if (self.esAfnd()):
            # Lógica de conversión
            print("uwu")
        else:
            return self

    def simplificarAfd(self):
        print("Simplificar autómata")
        # Lógica de simplificación

    def operar(self, operacion, automata):
        print("Obtener autómata a partir de una operación")
        if (operacion == "complemento"):
            print("Operación corresponde a complemento")
            # Lógica del complemento
        elif (operacion == "interseccion"):
            print("Operación corresponde a intersección")
            # Lógica de la intersección
        elif (operacion == "union"):
            print("Operación corresponde a unión")
            # Lógica de la unión
        elif (operacion == "concatenacion"):
            print("Operación corresponde a concatenación")
            # Lógica de la concatenación