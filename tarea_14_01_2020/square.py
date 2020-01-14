import math
import itertools


def square(p1, p2):
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return dist


def cuadro(points):
    lados = []
    for x, y in itertools.combinations(points, 2):
        lados.append(square(x, y))
    if len(list(set(lados))) != 2:
        print("No es cuadrado")
    else:
        print("Es un cuadrado")
