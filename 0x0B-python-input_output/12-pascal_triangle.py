#!/ust/bin/python3
""" module pascal """


def pascal_triangle(n):
    """ function pascal """
    fila = [1]
    cero = [0]
    final = []

    for i in range(n):
        final.append(fila)
        fila = [i + d for i, d in zip(fila + cero, cero + fila)]

    return final
