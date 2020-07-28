from collections import OrderedDict
from servicios import fecha_y_hora


class AutomataFinito:
    def __init__(self, E, K, S, F, s):
        print(fecha_y_hora()+"[automatafinito.py] __init__()")
        self.E = E  # (Σ) Alfabeto
        self.K = K  # (K) Nodos
        self.S = S  # (S) Iniciales
        self.F = F  # (F) Finales
        self.s = s  # (δ) Conexiones

    def nodos_string(self):
        print(fecha_y_hora()+"[automatafinito.py] nodos_string()")
        return "K = {" + ", ".join(self.K) + "}"

    def alfabeto_string(self):
        print(fecha_y_hora()+"[automatafinito.py] alfabeto_string()")
        return "Σ = {" + ", ".join(self.E) + "}"

    def iniciales_string(self):
        print(fecha_y_hora()+"[automatafinito.py] iniciales_string()")
        return "S = {" + ", ".join(self.S) + "}"

    def finales_string(self):
        print(fecha_y_hora()+"[automatafinito.py] finales_string()")
        return "F = {" + ", ".join(self.F) + "}"

    def conexiones_string(self):
        print(fecha_y_hora()+"[automatafinito.py] conexiones_string()")
        return "δ = {" + str(self.s) + "}"

    def mostrar_quintupla(self):
        print(fecha_y_hora()+"[automatafinito.py] mostrar_quintupla()")
        print(self.nodos_string())
        print(self.alfabeto_string())
        print(self.iniciales_string())
        print(self.finales_string())
        print(self.conexiones_string())

    def convertir_diccionario(self):
        print(fecha_y_hora()+"[automatafinito.py] convertir_diccionario()")
        return {
            "K": self.K,
            "E": self.E,
            "S": self.S,
            "F": self.F,
            "s": self.s
        }

    def es_afnd(self):
        print(fecha_y_hora()+"[automatafinito.py] es_afnd()")
        for conexion in self.s:
            if (conexion[1] == None):
                # Si la letra de esa arista es vacío
                return True
        return False

    def obtener_afd(self):
        print(fecha_y_hora()+"[automatafinito.py] obtener_afd()")
        nodos, inicio, finales, conexiones = transformacion(
            self.E, self.K, self.S, self.F, self.s)
        self.K = nodos
        self.S = inicio
        self.F = finales
        self.s = conexiones
        return AutomataFinito(self.E, nodos, inicio, finales, conexiones)

        # Lógica de conversión

    def simplificar_afd(self):
        print(fecha_y_hora()+"[automatafinito.py] simplificar_afd()")
        M = matriz_estados(self.E, self.K, self.F, self.s)
        I, A, D = enlaces(self.s)
        i = 0
        j = 0
        while(i < len(self.K)):
            j = 0
            while(j < len(self.K)):
                if(M[i][j] == 0):
                    if(self.K[i] in self.S):
                        reapuntar(self.K[i], self.K[j], D)
                        borracion(self.K[j], I, A, D)
                    else:
                        reapuntar(self.K[j], self.K[i], D)
                        borracion(self.K[i], I, A, D)
                    M[i][j] = 1
                    M[j][i] = 1
                j = j+1
            i = i+1
        self.K = delete(I, self.K)
        self.F = delete(I, self.F)
        self.s = decod(I, A, D)
        return self
        # Lógica de simplificación

    def union(self, automata1):
        print(fecha_y_hora()+"[automatafinito.py] union()")
        E = self.E.copy()
        K = self.K.copy()
        F = self.F.copy()
        s = self.s.copy()

        E = E + list(set(automata1.E) - set(E))
        K += automata1.K + ["Q0"]
        F += automata1.F
        s += automata1.s

        S = ["Q0"]
        s.append(("Q0", None, self.S[0]))
        s.append(("Q0", None, automata1.S[0]))

        print("Unión entre dos autómatas")
        # Lógica de la unión
        return AutomataFinito(E, K, S, F, s)

    def complemento(self):
        print(fecha_y_hora()+"[automatafinito.py] complemento()")
        if (not self.es_afnd()):
            # Es una propiedad sólo de AFD
            F = []
            K = self.K.copy()
            KsinInicial = self.K.copy()
            KsinInicial.remove(self.S[0])
            for nodo in KsinInicial:
                if (nodo not in self.F):
                    # Si el nodo no está en los finales del autómata
                    F.append(nodo)

            return AutomataFinito(self.E, K, self.S, F, self.s)
        else:
            print("El autómata debe ser AFD")
            return "El autómata debe ser AFD"

    def concatenacion(self, automata1):
        print(fecha_y_hora()+"[automatafinito.py] concatenacion()")
        E = self.E + list(set(automata1.E) - set(self.E))
        K = self.K.copy() + automata1.K.copy()
        F = automata1.F.copy()
        s = self.s.copy() + automata1.s.copy()
        S = self.S

        for final in self.F:
            s.append((final, None, automata1.S))

        return AutomataFinito(E, K, S, F, s)

    def interseccion(self, automata1):
        print(fecha_y_hora()+"[automatafinito.py] interseccion()")
        # ~(~A1 U ~A2)
        if (not self.es_afnd() and not automata1.es_afnd()):
            A1_complemento = self.complemento()
            A1_complemento.mostrar_quintupla()
            A2_complemento = automata1.complemento()
            A2_complemento.mostrar_quintupla()
            unido = A1_complemento.union(A2_complemento)
            unido.mostrar_quintupla()
            unido_afd = unido.obtener_afd()

            return unido_afd.complemento()
        else:
            return "Ambos autómatas deben ser AFD"

    def operar(self, operacion, automata1):
        print(fecha_y_hora()+"[automatafinito.py] operar(): Obtener autómata a partir de una operación")
        if (operacion == "complemento"):
            return self.complemento()
        elif (operacion == "interseccion"):
            return self.interseccion(automata1)
        elif (operacion == "union"):
            return self.union(automata1)
        elif (operacion == "concatenacion"):
            return self.concatenacion(automata1)


def buscar_id(variable, lista):
    print(fecha_y_hora()+"[automatafinito.py] buscar_id()")
    cont = 0
    for i in lista:
        if(i == variable):
            return cont
        cont = cont+1


def matriz(alfabeto, nodos):
    print(fecha_y_hora()+"[automatafinito.py] matriz()")
    matriz = []
    cont = 0
    for i in alfabeto:
        cont = cont+1
    for i in nodos:
        matriz.append([0]*cont)
    return matriz


def enlaces(conexiones):
    print(fecha_y_hora()+"[automatafinito.py] enlaces()")
    nd_inic = []
    alf_con = []
    nd_dest = []
    for i in conexiones:
        cont = 0
        for j in i:
            if(cont == 2):
                nd_dest.append(j)
                cont = cont+1
            if(cont == 1):
                alf_con.append(j)
                cont = cont+1
            if(cont == 0):
                nd_inic.append(j)
                cont = cont+1
    return nd_inic, alf_con, nd_dest


def llenar_matriz_c(nodos, alfabeto, conexiones):
    print(fecha_y_hora()+"[automatafinito.py] llenar_matriz_c()")
    M = matriz(alfabeto, nodos)
    I, A, D = enlaces(conexiones)
    n = 0
    while(n < len(I)):
        M[buscar_id(I[n], nodos)][buscar_id(A[n], alfabeto)] = D[n]
        n = n+1
    return M


def es_final(nodo, nodos, finales):
    print(fecha_y_hora()+"[automatafinito.py] es_final()")
    for i in finales:
        if(i == nodos[nodo]):
            return True
    return False


def matriz_estados(alfabeto, nodos, finales, conexiones):
    print(fecha_y_hora()+"[automatafinito.py] matriz_estados()")
    C = llenar_matriz_c(nodos, alfabeto, conexiones)
    E = matriz(nodos, nodos)
    i = 0
    j = 0
    while(i < len(nodos)):
        j = 0
        while(j < len(nodos)):

            if(i == j):
                E[i][j] = -1
            j = j+1
        i = i+1
    i = 0
    j = 0
    while(i < len(nodos)):
        j = 0
        while(j < len(nodos)):
            val = False
            if(j == i):
                j = j+1
                val = True
            elif(E[i][j] == 1):
                j = j+1
                val = True
            elif(es_final(i, nodos, finales) and not(es_final(j, nodos, finales))):
                E[i][j] = 1
                E[j][i] = 1
            else:
                a = C[j][0]
                b = C[i][0]
                if(E[buscar_id(a, nodos)][buscar_id(b, nodos)] == 1):
                    E[i][j] = 1
                    E[j][i] = 1
                else:
                    a = C[j][1]
                    b = C[i][1]
                    if(E[buscar_id(a, nodos)][buscar_id(b, nodos)] == 1):
                        E[i][j] = 1
                        E[j][i] = 1
            if(not val):
                j = j+1
        i = i+1
    return E


def reapuntar(mantener, borrar, destinos):
    print(fecha_y_hora()+"[automatafinito.py] reapuntar()")
    indice = 0
    for i in destinos:
        if(i == borrar):
            destinos[indice] = mantener
        indice = indice+1


def borracion(borrar, partidas, caminos, destinos):
    print(fecha_y_hora()+"[automatafinito.py] borracion()")
    i = 0
    while(i < len(partidas)):
        val = False
        if(partidas[i] == borrar):
            partidas.pop(i)
            caminos.pop(i)
            destinos.pop(i)
            val = True
        if(not val):
            i = i+1


def delete(partidas, nodos):
    print(fecha_y_hora()+"[automatafinito.py] delete()")
    i = 0
    while(i < len(nodos)):
        val = False
        if(nodos[i] not in partidas):
            nodos.pop(i)
            val = True
        if(not val):
            i = i+1
    return(nodos)


def decod(partidas, caminos, destinos):
    print(fecha_y_hora()+"[automatafinito.py] decod()")
    lista = []
    i = 0
    while(i < len(partidas)):
        tupla = (partidas[i], caminos[i], destinos[i])
        lista.append(tupla)
        i = i+1
    return lista


def matE_AFND(alfabeto, nodos):
    print(fecha_y_hora()+"[automatafinito.py] matE_AFND()")
    matriz = []
    cont = 0
    for i in alfabeto:
        cont = cont+1
    for i in nodos:
        matriz.append([0]*cont)
    i = 0
    while(i < len(nodos)):
        j = 0
        while(j < len(alfabeto)):
            matriz[i][j] = []
            j += 1
        i += 1
    return matriz


def conx_void(nodo, partidas, caminos):
    print(fecha_y_hora()+"[automatafinito.py] conx_void()")
    i = 0
    cont = 0
    while(i < len(partidas)):
        if(partidas[i] == nodo):
            if(caminos[i] == None):
                return True
        i += 1
    return False


def caminos_void(nodo, partidas, caminos, destinos):
    print(fecha_y_hora()+"[automatafinito.py] caminos_void()")
    i = 0
    lista = []
    while(i < len(partidas)):
        if(partidas[i] == nodo and caminos[i] == None):
            lista.append(destinos[i])
        i += 1
    return lista


def buscar_destino(nodo, camino, partidas, caminos, destinos):
    print(fecha_y_hora()+"[automatafinito.py] buscar_destino()")
    i = 0
    while(i < len(partidas)):
        if(partidas[i] == nodo and caminos[i] == camino):
            return destinos[i]
        i += 1
    return "sumidero"


def buscar_conxVoid(nodo, camino, partidas, caminos, destinos):
    print(fecha_y_hora()+"[automatafinito.py] buscar_conxVoid()")
    cant = 0
    V = caminos_void(nodo, partidas, caminos, destinos)
    cantidadV = len(V)
    estacosa = ""
    while(cant < cantidadV):
        estacosa = estacosa + "|" + \
            buscar_destino(V[cant], camino, partidas, caminos, destinos)+"|"
        if(conx_void(V[cant], partidas, caminos)):
            estacosa = estacosa + "|" + \
                buscar_conxVoid(V[cant], camino, partidas,
                                caminos, destinos) + "|"
        cant += 1
    return estacosa


def dest_to_list(estacosa):
    print(fecha_y_hora()+"[automatafinito.py] dest_to_list()")
    i = 0
    lista = []
    aux = ""
    mod = False
    while(i < len(estacosa)):
        val = False
        if(estacosa[i] != "|"):
            aux = aux+estacosa[i]
            mod = True
        if(estacosa[i] == "|" and mod):
            mod = False
            lista.append(aux)
            aux = ""
        i += 1
    return lista


def llenar_matCAFND(nodos, alfabeto, conexiones):
    print(fecha_y_hora()+"[automatafinito.py] llenar_matCAFND()")
    M = matE_AFND(alfabeto, nodos)
    I, A, D = enlaces(conexiones)
    n = 0
    while(n < len(I)):
        if(A[n] != None):
            M[buscar_id(I[n], nodos)][buscar_id(A[n], alfabeto)].append(D[n])
        if(conx_void(D[n], I, A)):
            aux = caminos_void(D[n], I, A, D)
            for i in aux:
                M[buscar_id(I[n], nodos)][buscar_id(A[n], alfabeto)].append(i)
        if(A[n] == None):
            letra = 0
            while(letra < len(alfabeto)):
                aux = dest_to_list(buscar_conxVoid(
                    I[n], alfabeto[letra], I, A, D))
                for i in aux:
                    M[buscar_id(I[n], nodos)][buscar_id(
                        alfabeto[letra], alfabeto)].append(i)
                letra += 1

        n = n+1
    i = 0
    while(i < len(nodos)):
        j = 0
        while(j < len(alfabeto)):
            M[i][j] = list(OrderedDict.fromkeys(M[i][j]))
            j += 1
        i += 1
    return M


def union_nodos(unir):
    print(fecha_y_hora()+"[automatafinito.py] union_nodos()")
    aux = ""
    for i in unir:
        aux += i
    return aux


def separar(nodo, nodos):
    print(fecha_y_hora()+"[automatafinito.py] separar()")
    aux = ""
    lista = []
    i = 0
    while(i < len(nodo)):
        aux += nodo[i]
        if(aux in nodos):
            lista.append(aux)
            aux = ""
        i += 1
    return lista


def cant_destinos(id_nodo, matriz, camino):
    print(fecha_y_hora()+"[automatafinito.py] cant_destinos()")
    return len(matriz[id_nodo][camino])


def separar_caminos(conexion, nodos, guia, conexiones):
    print(fecha_y_hora()+"[automatafinito.py] separar_caminos()")
    Nnodos = []
    auxP = []
    auxC = []
    auxD = []
    auxP.append(conexion[0])
    i = 0
    while(i < len(conexion[1])-1):
        auxC.append(conexion[1][i])
        auxD.append("zz00"+str(guia))
        if(("zz00"+str(guia)) not in Nnodos):
            Nnodos.append("zz00"+str(guia))
        auxP.append("zz00"+str(guia))
        guia += 1
        i += 1
    auxC.append(conexion[1][i])
    auxD.append(conexion[2])
    Laux = []
    ConxAUX = decod(auxP, auxC, auxD)
    i = 0
    while(i < len(conexiones)):
        if(conexiones[i] == conexion):
            j = i+1
            while(j < len(conexiones)):
                Laux.append(conexiones[j])
                j += 1
            while(i < len(conexiones)):
                conexiones.pop()
        i += 1
    for i in ConxAUX:
        conexiones.append(i)
    for i in Laux:
        conexiones.append(i)
    for i in Nnodos:
        nodos.append(i)


def transformacion(alfabeto, nodos, iniciales, finales, conexiones):
    print(fecha_y_hora()+"[automatafinito.py] transformacion()")
    i = 0
    guia = 1
    while(i < len(conexiones)):
        if(conexiones[i][1] != None):
            if(len(conexiones[i][1]) > 1):
                separar_caminos(conexiones[i], nodos, guia, conexiones)
        i += 1
    M = llenar_matCAFND(nodos, alfabeto, conexiones)
    P, C, D = enlaces(conexiones)
    nodosAFD = []
    inicialAFD = []
    finalesAFD = []
    conexionesAFD = []
    Pafd = []
    Cafd = []
    Dafd = []
    AUX = caminos_void(iniciales[0], P, C, D)
    for i in AUX:
        iniciales.append(i)
    inicialAFD.append(union_nodos(iniciales))
    nodosAFD.append(union_nodos(iniciales))
    i = 0
    while(i < len(nodos)):
        j = 0
        while(j < len(alfabeto)):
            if((union_nodos(M[i][j]) not in nodosAFD) and (union_nodos(M[i][j]) != "")):
                nodosAFD.append(union_nodos(M[i][j]))
            j += 1
        i += 1
    i = 0
    while(i < len(nodosAFD)):
        L = separar(nodosAFD[i], nodos)
        abc = 0
        while(abc < len(alfabeto)):
            aux = ""
            val = False
            Laux = []
            Void = []
            for j in L:
                if(conx_void(buscar_destino(j, alfabeto[abc], P, C, D), P, C)):
                    Void = caminos_void(buscar_destino(
                        j, alfabeto[abc], P, C, D), P, C, D)
                    for k in Void:
                        Laux.append(k)
                if(buscar_destino(j, alfabeto[abc], P, C, D) != "sumidero"):
                    Laux.append(buscar_destino(j, alfabeto[abc], P, C, D))
            Laux = sorted(Laux)
            Laux = list(OrderedDict.fromkeys(Laux))
            for k in Laux:
                aux += k
            Pafd.append(nodosAFD[i])
            Cafd.append(alfabeto[abc])
            if(aux == ""):
                Dafd.append("sumidero")
                if("sumidero" not in nodosAFD):
                    nodosAFD.append("sumidero")
            else:
                Dafd.append(aux)
            if((aux not in nodosAFD) and aux != ""):
                nodosAFD.append(aux)
            abc += 1
        i += 1
    i = 0
    while(i < len(nodosAFD)):
        L = separar(nodosAFD[i], nodos)
        for j in L:
            if(j in finales):
                finalesAFD.append(nodosAFD[i])
        i += 1
    finalesAFD = list(OrderedDict.fromkeys(finalesAFD))
    conexionesAFD = decod(Pafd, Cafd, Dafd)
    return nodosAFD, inicialAFD, finalesAFD, conexionesAFD
