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

# Calcular la diferencia de bits usando sin usar Huffman vs usandolo.
def diferencia(datos, codigo):
    pre_huffman = len(datos)*8
    post_huffman = 0
    claves = codigo.keys()
    for i in claves:
        contar = datos.count(i)
        post_huffman += contar * len(codigo[i]) # Calculo de numero de bits necesarios
        

    return "El almacaneamiento antes de compresion (bits):", pre_huffman, "\nEl almacenamiento despues de compresion (bits):", post_huffman

def codigo_huffman(datos):
    # crear_dict = calcular_diccionario(datos) """Crea un diccionario en base a los datos, en este caso ya creamos el diccionario para pasar valores."""

    letras = datos.keys()

    nodos = []

    for letra in letras:
        nodos.append(Node(datos.get(letra), letra))

    while len(nodos) > 1:

        # ordenamos los nodos de manera ascendente
        nodos = sorted(nodos, key=lambda x: x.probabilidad)

        # cogemos los nodos mas pequeños
        der = nodos[0]
        izq = nodos[1]

        izq.codigo = 0
        der.codigo = 1

        # juntamos los nodos pequeños para crear un nuevo nodo
        nuevo_nodo = Node(izq.probabilidad+der.probabilidad, izq.simbolo+der.simbolo, izq, der)

        nodos.remove(izq)
        nodos.remove(der)
        nodos.append(nuevo_nodo)

    codigo_huffman = calculo_codificacion(nodos[0])
    # print(diferencia(datos, codigo_huffman))
    codigo_final = codificar(datos, codigo_huffman)

    return codigo_final, nodos[0]

def decodificar_huffman(datos, huffman):
    raiz = huffman
    decode = []

    for x in datos:
        if x =="1":
            huffman = huffman.der
        elif x =="0":
            huffman = huffman.izq

        try:
            if huffman.izq.simbolo == None and huffman.der.simbolo == None:
                pass

        except AttributeError:
            decode.append(huffman.simbolo)
            huffman = raiz

    formato = "".join([str(valor) for valor in decode])
    return formato


# datos = {"A":11, "B":2, "C":4, "D":3, "E":14, "G":3, "I":6, "L":6, "M":3, "N":6, "O":7, "P":4, "Q":1, "R":10, "S":4, "T":3, "U":4, "V":2, " ":17, ",":2}

if __name__ == "__main__":

    datos = {"A":11, "B":2, "C":4, "D":3, "E":14, "G":3, "I":6, "L":6, "M":3, "N":6, "O":7, "P":4, "Q":1, "R":10, "S":4, "T":3, "U":4, "V":2, " ":17, ",":2}
    codigo = codigo_huffman(datos)
    print("Codificacion final:", codigo[0])
    mensaje1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    mensaje2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    decodificar1 = decodificar_huffman(mensaje1, codigo[1])
    decodificar2 = decodificar_huffman(mensaje2, codigo[1])
    print("El primer mensaje resuelto es:", decodificar1)
    print("El segundo mensaje resuleto es:", decodificar2)   
        

