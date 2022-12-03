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

def calculo_codificacion(nodo, valor=""):

    nuevo_valor = valor + str(nodo.codigo)

    if nodo.izq:
        calculo_codificacion(nodo.izq, nuevo_valor)
    
    if nodo.der:
        calculo_codificacion(nodo.der, nuevo_valor)

    if not nodo.izq and not nodo.der:
        codificacion[nodo.simbolo] = nuevo_valor

    return codificacion

# Esta funcion sirve para cuando nos dan un string tal que: AAABBBCC.
# De esta manera convierte el string en un diccionario con la cantidad de repeticiones por cada letra.
# En este caso utilizamos pasamos un diccionario directamente a la funcion Huffman y no un string pero se
# podria utilizar de esta manera.

def calcular_diccionario(datos):
    simbolos = dict()

    for valor in datos:
        if simbolos.get(valor)==None:
            simbolos[valor] = 1
        else:
            simbolos[valor] += 1

    return simbolos

def codificar(datos, codigo):

    datos_codificados = []

    for c in datos:
        datos_codificados.append(codigo[c])

    formato = "".join([str(valor) for valor in datos_codificados])

    return formato

def diferencia(datos, codigo):
    pre_huffman = len(datos)*8
    post_huffman = 0
    claves = codigo.keys()
    for i in claves:
        contar = datos.count(i)
        post_huffman += contar * len(codigo[i]) # Calculo de numero de bits necesarios
        
    return pre_huffman, post_huffman

def codigo_huffman(datos):
    # crear_dict = calcular_diccionario(datos); Crea un diccionario en base a los datos, en este caso ya creamos el diccionario para pasar valores.

    letras = datos.keys()
    valores = datos.values()

    nodos = []

    for letra in letras:
        nodos.append(Node(datos.get(letra), letra))

    while len(nodos) > 1:

        # ordenamos los nodos de manera ascendente
        nodos = sorted(nodos, key=lambda x: x.prob)

        # cogemos los nodos mas pequeños
        der = nodos[0]
        izq = nodos[1]

        izq.codigo = 0
        der.codigo = 1

        # juntamos los nodos pequeños para crear un nuevo nodo
        nuevo_nodo = Node(izq.)


