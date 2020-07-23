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
        M=matriz_estados(self.E,self.K,self.F,self.s)
        I,A,D=enlaces(self.s)
        i=0
        j=0
        while(i<len(self.K)):
            j=0
            while(j<len(self.K)):
                if(M[i][j]==0):
                    if(self.K[i] in self.S):
                        reapuntar(self.K[i],self.K[j],D)
                        borracion(self.K[j],I,A,D)
                    else:
                        reapuntar(self.K[j],self.K[i],D)
                        borracion(self.K[i],I,A,D)
                    M[i][j]=1
                    M[j][i]=1
                j=j+1
            i=i+1
        self.K=delete(I,self.K)
        self.F=delete(I,self.F)
        self.s=decod(I,A,D)
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

def buscar_id(variable,lista):
    cont = 0
    for i in lista:
        if(i==variable):
            return cont
        cont=cont+1
def matriz(alfabeto,nodos):
    matriz=[]
    cont=0
    for i in alfabeto:
        cont=cont+1
    for i in nodos:
        matriz.append([0]*cont)
    return matriz
def enlaces(conexiones):
    nd_inic=[]
    alf_con=[]
    nd_dest=[]
    for i in conexiones:
        cont=0
        for j in i:
            if(cont==2):
                nd_dest.append(j)
                cont=cont+1
            if(cont==1):
                alf_con.append(j)
                cont=cont+1
            if(cont==0):
                nd_inic.append(j)
                cont=cont+1 
    return nd_inic,alf_con,nd_dest
        
def llenar_matrizC(nodos,alfabeto,conexiones):
    M=matriz(alfabeto,nodos)
    I,A,D=enlaces(conexiones)
    n=0
    while(n<len(I)):
        M[buscar_id(I[n],nodos)][buscar_id(A[n],alfabeto)]=D[n]
        n=n+1
    return M
def es_final(nodo,nodos,finales):
    for i in finales:
        if(i==nodos[nodo]):
            return True
    return False

def matriz_estados(alfabeto,nodos,finales,conexiones):
    C=llenar_matrizC(nodos,alfabeto,conexiones)
    E=matriz(nodos,nodos)
    i=0
    j=0
    while(i<len(nodos)):
        j=0
        while(j<len(nodos)):
            
            if(i==j):
                E[i][j]=-1
            j=j+1
        i=i+1
    i=0
    j=0
    while(i<len(nodos)):
        j=0
        while(j<len(nodos)):
            val=False
            if(j==i):
                j=j+1
                val=True
            elif(E[i][j]==1):
                j=j+1
                val=True
            elif(es_final(i,nodos,finales) and not(es_final(j,nodos,finales))):
                E[i][j]=1
                E[j][i]=1
            else:
                a=C[j][0]
                b=C[i][0]
                if(E[buscar_id(a,nodos)][buscar_id(b,nodos)] == 1):
                    E[i][j]=1
                    E[j][i]=1
                else:
                    a=C[j][1]
                    b=C[i][1]
                    if(E[buscar_id(a,nodos)][buscar_id(b,nodos)] == 1):
                        E[i][j]=1
                        E[j][i]=1
            if(not val):
                j=j+1
        i=i+1
    return E

def reapuntar(mantener,borrar,destinos) :
    indice=0
    for i in destinos:
        if(i==borrar):
            destinos[indice]=mantener
        indice=indice+1
def borracion(borrar, partidas, caminos, destinos):
    i=0
    while(i<len(partidas)):
        val=False
        if(partidas[i]==borrar):
            partidas.pop(i)
            caminos.pop(i)
            destinos.pop(i)
            val=True
        if(not val):
            i=i+1

def delete(partidas,nodos):
    i=0
    while(i<len(nodos)):
        val=False
        if(nodos[i] not in partidas):
            nodos.pop(i)
            val=True
        if(not val):
            i=i+1
    return(nodos)
    
def decod(partidas,caminos,destinos):
    lista=[]
    i=0
    while(i<len(partidas)):
        tupla=(partidas[i],caminos[i],destinos[i])
        lista.append(tupla)
        i=i+1
    return lista
