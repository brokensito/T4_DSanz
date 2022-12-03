import doctest
import math

# En este ejercicio desarrollaremos diferentes metodos para encontrar la raiz de una funcion y calcular 
# el numero de iteraciones posibles en cada caso.

# Primero definimos la funcion
def f(x):
    return x**3 + x + 16
    
# Definimos la funcion biseccion segun la formula, utilizando un contador para el numero de iteraciones y 
# poniendo una condicion en base al margen de error.
def biseccion(a,b,error):
    """
    >>> print(biseccion(-5,-1,0.001))
    ('La raiz buscada es', -2.3876953125, 'con', 13, 'veces iteradas.')

    """
    iteraciones = 1
    condicion = True

    while condicion:
        c = (a+b)/2

        if f(a) * f(c) < 0:
            b = c
        else: 
            a = c
        
        iteraciones += 1
        condicion = abs(f(c)) > error
        
    return "La raiz buscada es", c , "con", iteraciones, "veces iteradas."


# Definimos la funcion segun la formula de la misma manera que la funcion anterior utilizando un contador y 
def secante(a, b, error):
    """
    >>> print(secante(-5,-1,0.001))
    ('La raiz buscada es', -2.3876708156864592, 'con', 8, 'veces iteradas.')

    """
    iteraciones = 1
    condicion = True
    while condicion:
        if f(a) == f(b):
            print( "No se puede continuar, error (0).")
            break

        c = a - (b-a)*f(a)/( f(b) - f(a) )
        a = b
        b = c
        iteraciones +=1

        condicion = abs(f(c)) > error

    return "La raiz buscada es", c, "con", iteraciones, "veces iteradas."

# Primero definimos la derivada de la funcion
def h(x):
    return 4

# Definimos la funcion en base al metodo newtonraphson
def newtonraphson(a, error):
    """
    >>> print(newtonraphson(-5,0.001))
    ('La raiz buscada es', -4.0, 'con', 2, 'veces iteradas.')
    
    """
    iteraciones = 1
    condicion = True

    while condicion:
        if h(a) == 0.0:
            print("Error, no se puede calcular.")
            break

        b = a - f(a)/h(a)
        a = b
        iteraciones+=1
        condicion = abs(f(b))>error

    return "La raiz buscada es", b, "con", iteraciones, "veces iteradas."




if __name__=="__main__":
    doctest.testmod()




