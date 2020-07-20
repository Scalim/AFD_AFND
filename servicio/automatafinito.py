class AutomataFinito:
    def __init__(self, E, K, S, F, s):
        self.E = E  # (Σ) Alfabeto
        self.K = K  # (K) Nodos
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

    def union(self, automata1, automata2):
        E = automata1.E.copy()
        K = automata1.K.copy()
        F = automata1.F.copy()
        s = automata1.s.copy()

        E + automata2.E
        K + automata2.K
        F + automata2.F
        s + automata2.s

        S = "Q0"
        s.append(("Q0", None, automata1.S))
        s.append(("Q0", None, automata2.S))

        print("Unión entre dos autómatas")
        # Lógica de la unión
        return AutomataFinito(E, K, S, F, s)

    def complemento(self, automata):
        if (not automata.esAfnd):
            # Es una propiedad sólo de AFD
            F = []
            K = automata.K.copy()
            KsinInicial = K.remove(automata.S)
            for nodo in KsinInicial:
                if (nodo not in automata.F):
                    # Si el nodo no está en los finales del autómata
                    F.append(nodo)

            return AutomataFinito(automata.E, automata.K, automata.S, automata.F, automata.s)
        else:
            raise Exception("El autómata debe ser AFD")

    def concatenacion(self, automata1, automata2):
        E = automata1.E.copy() + automata2.E.copy()
        K = automata1.K.copy() + automata2.K.copy()
        F = automata2.F.copy()
        s = automata1.s.copy() + automata2.s.copy()
        S = automata1.S

        for final in automata1.F:
            s.append((final, None, automata2.S))

        return AutomataFinito(E, K, S, F, s)

    def interseccion(self, automata1, automata2):
        # ~(~A1 U ~A2)
        if (not automata1.esAfnd() and not automata2.esAfnd()):
            return self.complemento(self.union(self.complemento(automata1), self.complemento(automata2)))
        else:
            raise Exception("Ambos autómatas deben ser AFD")

    def operar(self, operacion, automata1, automata2):
        print("Obtener autómata a partir de una operación")
        if (operacion == "complemento"):
            self.complemento(automata1)
        elif (operacion == "interseccion"):
            self.interseccion(automata1, automata2)
        elif (operacion == "union"):
            self.union(automata1, automata2)
        elif (operacion == "concatenacion"):
            self.concatenacion(automata1, automata2)