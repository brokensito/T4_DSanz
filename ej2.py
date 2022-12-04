import numpy as np

class Mision():
    def __init__(self, mision,tipo, planeta, general):
        self.mision = mision
        self. tipo = tipo
        self.planeta = planeta
        self.general = general


def asignacion(datos):

    vehiculos1 = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
    vehiculos2 = vehiculos1 + [ "AT-M6", "AT-MP", "AT-DT"]

    resultados = {}

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

        pregunta = input("¿\nDesea seguir (SI) o agregar una nueva mision (NO) ? ")

        if pregunta == "SI":
            pass

        else:
            mision = input("Introduzca el nombre de la mision.")
            tipo = input("Introduzca el tipo de la mision.")
            planeta = input("Introduza el destino de la mision.")
            general = input("Introduzca quien le ecomiendo la mision.")
            datos.append(Mision(mision, tipo, planeta, general))



    return resultados

def recursos(datos):

    valores = []
    for i in datos:
        


if __name__ == "__main__":































if __name__=="__main__":

    misiones = [Mision("Palpatine")]


