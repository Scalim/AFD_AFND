class AutomataFinito:
    def __init__(self, E, K, S, F, s):
        self.E = E  # (Σ) Alfabeto
        self.K = K  # (K) Nodos
        self.S = S  # (S) Iniciales
        self.F = F  # (F) Finales
        self.L = s  # (δ) Conexiones

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

    def union(automata1, automata2):
        # Lógica de la unión

    def complemento(automata):
        if (not automata.esAfnd):
            # Es una porpiedad sólo de AFD
            F = []
            K = automata.K.copy()
            KsinInicial = K.remove(automata.S)
            for nodo in KsinInicial:
                if (nodo not in automata.F):
                    # Si el nodo no está en los finales del autómata
                    F.append(nodo)

            return AutomataFinito(automata.E, automata.K, automata.S, F, automata.s)
        else:
            raise Exception("El autómata debe ser AFD")

    def concatenacion(automata1, automata2):
        # Lógica de la concatenación

    def interseccion(automata1, automata2):
        # ~(~A1 U ~A2)
        if (not automata1.esAfnd() and not automata2.esAfnd()):
            return complemento(union(complemento(automata1), complemento(automata2)))
        else:
            raise Exception("Ambos autómatas deben ser AFD")

    def operar(self, operacion, automata):
        if (operacion == "complemento"):
            complemento(self, automata)
        elif (operacion == "interseccion"):
            interseccion(self, automata)
        elif (operacion == "union"):
            union(self, automata)
        elif (operacion == "concatenacion"):
            concatenacion(self, automata)
