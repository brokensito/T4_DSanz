import doctest
# En este ejercicio desarrollaremos diferentes metodos para encontrar la raiz de una funcion y calcular 
# el numero de iteraciones posibles en cada caso.

# Primero definimos la funcion
def f(x):
    return x**2 + x + 16
    

def biseccion(a,b,error):
    iteraciones = 0
    condicion = True

    while condicion:
        c = (a+b)/2

        if f(a) * f(c) < 0:
            b = c
        else: 
            a = c
        
        iteraciones += 1
        condicion = abs(f(c)) > error
        
    return "La raiz buscada es", c , "con", iteraciones, "iteraciones."

print(biseccion(-3,-1,0.05))






# if __name__=="__main__":
#     doctest.testmod()



