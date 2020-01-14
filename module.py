opciones = {"1.Sumar": lambda x: print(x), "2.Restar": lambda y: print(y)}


def menu(options):
    print("Bienvenido al menu!")
    print("\n".join(list(opciones.keys())))

    return list(opciones.values())[int(input("Elija su opcion:")) - 1]


menu(opciones)("Test function")
