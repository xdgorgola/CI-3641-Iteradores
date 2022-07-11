import sys

def bienParentizadas(n):
    """
    General todas las posibles expresiones bien 
    parentizadas para pares de parentesis

    Arguments:
        n -- Numero de parentesis

    Yields:
        Una expresion bien parentizada
    """

    for i in bienAux(n, n):
        yield i


def bienAux(a, c):
    """
    Funcion auxiliar para bien parentizadas. Devuelve
    todas las expresiones con parentesis que le falten
    a parentesis por abrir y c parentesis por cerrar

    Arguments:
        a -- Numero de parentesis abiertos que faltan
        c -- Numero de parentesis cerrados que faltan

    Yields:
        Expresion parentizada que contenga a parentesis por abrir
        y c parentesis por cerrar
    """

    if (a == c and c == 0):
        yield ""
    else:
        # cerramos parentesis si aun hay que cerrar
        if (c > a):
            for i in bienAux(a, c - 1):
                yield f"){i}"

        # abrimos parentesis
        if (a > 0):
            for i in bienAux(a - 1, c):
                    yield f"({i}"


for i in bienParentizadas(int(sys.argv[1])):
    print(i)