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