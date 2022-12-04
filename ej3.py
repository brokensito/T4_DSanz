import sys

class Graph(object):
    def __init__(self, nodos, g_inicial):
        self.nodos = nodos
        self.grafo = self.construir_grafo(nodos, g_inicial)


    def construir_grafo(self, nodos, g_inicial):

        grafo = {}

        for nodo in nodos:
            grafo[nodo] = {}

        grafo.update(g_inicial)

        for nodo, vertice in grafo.items():
            for nodo_contiguo, valor in vertice.items():
                if grafo[nodo_contiguo].get(nodo, False)==False:
                    grafo[nodo_contiguo][nodo] = valor

        return grafo

    def sacar_nodos (self):
        # Nos da los nodos del grafo.
        return self.nodos

    def sacar_vertices(self, nodo):
        # Sacamos los nodos vecinos
        conexiones = []
        for nodo_exterior in self.nodos:
            if self.grafo[nodo].get(nodo_exterior, False)!=False:
                conexiones.append(nodo_exterior)

        return conexiones

    def diferencia(self, nodo1, nodo2):
        # Nos da la diferencia entre nodos
        return self.grafo[nodo1][nodo2]

def djikstra(grafo, n_inicial):

    no_visitados = list(grafo.sacar_nodos())

    # Creamos un diccionario para guardar el camino mas corto a medida que recorremos el grafo
    camino_corto = {}

    # Creamos otro diccionario para guardar el camino mas corto hasa dicho momento
    nodos_previos = {}

    max_value = sys.maxsize
    for nodo in no_visitados:
        camino_corto[nodo] = max_value

    camino_corto[n_inicial] = 0

    while no_visitados:

        min_actual = None
        for nodo in no_visitados:
            if min_actual==None:
                min_actual = nodo

            elif camino_corto[nodo] < camino_corto[min_actual]:
                min_actual = nodo


        vecinos = grafo.sacar_vertices(min_actual)
        for vecino in vecinos:
            valor_posible = camino_corto[min_actual] + grafo.diferencia(min_actual, vecino)
            if valor_posible < camino_corto[vecino]:

                camino_corto[vecino] = valor_posible

                # Actualizamos la mejor ruta
                nodos_previos[vecino] = min_actual
        
        no_visitados.remove(min_actual)

    return nodos_previos, camino_corto


def mostrar(nodos_previos, camino_corto, n_inicial, n_final):
    camino = []
    nodo = n_final

    while nodo != n_inicial:
        camino.append(nodo)
        nodo = nodos_previos[nodo]

    camino.append(n_inicial)

    print("El camino corto posible es: {}".format(camino_corto[n_final]))
    print(" --> ".join(reversed(camino)))


if __name__=="__main__":

    nodos = [
        "Kings Cross",

     "Waterloo", 

     "Victoria Train Station",

      "Liverpool Street Station",

       "St.Pancras",

        "London Eye"
        ]

    g_inicial = {}
    for nodo in nodos:
        g_inicial[nodo] = {}

    g_inicial["Victoria Train Station"]["London Eye"] = 2
    g_inicial["St.Pancras"]["Victoria Train Station"] = 3
    g_inicial["St.Pancras"]["Liverpool Street Station"] = 1
    g_inicial["Victoria Train Station"]["St.Pancras"] = 7
    g_inicial["Liverpool Street Station"]["Waterloo"] = 10
    g_inicial["London Eye"]["Waterloo"] = 4
    g_inicial["London Eye"]["Kings Cross"] = 4

    grafo = Graph(nodos, g_inicial)

    nodos_previos, camino_corto = djikstra(grafo=grafo, n_inicial="Kings Cross")
    mostrar(nodos_previos, camino_corto, n_inicial="Kings Cross", n_final="Waterloo")

    nodos_previos, camino_corto = djikstra(grafo=grafo, n_inicial="Victoria Train Station")
    mostrar(nodos_previos, camino_corto, n_inicial="Victoria Train Station", n_final="Liverpool Street Station")

    nodos_previos, camino_corto = djikstra(grafo=grafo, n_inicial="St.Pancras")
    mostrar(nodos_previos, camino_corto, n_inicial="St.Pancras", n_final="Kings Cross")

    


