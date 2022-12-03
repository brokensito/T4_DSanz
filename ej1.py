class Node:

    def __init__(self, probabilidad, simbolo, izq=None, der=None):
        # probabilidad
        self.probabilidad = probabilidad

        # simbolo
        self.simbolo = simbolo

        # izquierda nodo
        self.izq = izq

        # derecha nodo
        self.der = der

        # apuntamiento nodo
        self.codigo = ""

codificacion = dict()

