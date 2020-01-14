import module
import menu
import square

opciones = {"1.Sumar": lambda x: print(x), "2.Restar": lambda y: print(y)}
puntos = [(0, 1), (0, 2), (2, 2), (2, 0)]

if __name__ == "__main__":
    print("<---------Problema 22----------->")
    module.loops(module.read('triangle.txt'))
    print("<---------Problema 23----------->")
    square.cuadro(puntos)
    print("<-------------Menu-------------->")
    menu.menu(opciones)("Test function")
