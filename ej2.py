import numpy as np
# Primero creamos las diferentes misiones pasandole los argumentos requeridos
class Mision():
    def __init__(self, mision,tipo, planeta, general):
        self.mision = mision
        self. tipo = tipo
        self.planeta = planeta
        self.general = general

# Creamos una funcion para asignar las misiones
def asignacion(datos):

    vehiculos1 = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
    vehiculos2 = vehiculos1 + [ "AT-M6", "AT-MP", "AT-DT"]

    # Creamos una lista para pasar las posibles nuevas misiones y un diccionario para almacenar los datos de asignacion.
    nuevas_misiones = []
    resultados = {}

    # Iteramos la lista de misiones para saber de que general vienen y actuar segun su tipo
    for c in datos:

        if c.general == "Darth Vader" or c.general == "Palpatine":
            resultados[c.mision] = ("Asignacion manual.")
            
        else:
            if c.tipo=="Exploracion":
                resultados[c.mision] = 15, "scout troopers y", 2 ," speeder bike."

            elif c.tipo == "Contencion":
                resultados[c.mision] = 30, "storm troopers y", 3 ," vehiculos ( ", np.random.choice(vehiculos1, 3), " )."

            elif c.tipo == "Ataque":
                resultados[c.mision] = 50, "storm troopers y", 7, " vehiculos ( ", np.random.choice(vehiculos2,7), " )."

        # Preguntamos si quieres seguir o agregar una nueva mision
        pregunta = input("¿\nDesea seguir (SI) o agregar una nueva mision (NO) ? ")

        if pregunta == "SI":
            pass

        else:
            mision = input("Introduzca el nombre de la mision.")
            tipo = input("Introduzca el tipo de la mision.")
            planeta = input("Introduza el destino de la mision.")
            general = input("Introduzca quien le ecomiendo la mision.")
            nuevas_misiones.append(Mision(mision, tipo, planeta, general))

    if nuevas_misiones!=None:
        asignacion(nuevas_misiones)

    # Llamamos a la funcion recursos para ver las tropas utilizadas.
    suma = recursos(resultados)

    return resultados, suma

# Creamos una funcion para almacenar la cantida de recursos utilizados
def recursos(datos):

    valores = []
    for i in datos.values():
        valores.append(i[0])
        valores.append(i[2])

    return(sum(valores))

def mostrar(datos):
    for i in datos[0]:
        sol = print("\nLa mision", i, "ha utilizado", datos[i])
        print("-----------------------------------------------------------------------")

    print("El total de recursos ha sido", datos[1])

    return sol




if __name__ == "__main__":
    misiones = [
        Mision("Aprobar Algoritmos","Ataque","Jedha","Ruben Juarez"),
        Mision("Conquistar Marte","Contencion","Bespin","Darth Vader"),
        Mision("Ataque al Emperador Sith","Ataque","Trandosha","General Grievous"),
        Mision("Batalla de Scipio","Exploracion","Umbara","Palpatine"),
    ]

    solucion = asignacion(misiones)
    mostrar(solucion)































if __name__=="__main__":

    misiones = [Mision("Palpatine")]


