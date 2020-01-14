import math
import itertools

puntos = [(0, 1), (0, 2), (2, 2), (2,0)]

def square(p1,p2):
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return dist

def cuadro(points):
    lados = []
    for x, y in itertools.combinations(points, 2):
       lados.append(square(x, y))
    return len(list(set(lados)))

if cuadro(puntos) != 2:
    print("No es cuadrado")
else:
    print("Es un cuadrado")