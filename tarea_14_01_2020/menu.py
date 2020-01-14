def menu(options):
    print("Bienvenido al menu!")
    print("\n".join(list(options.keys())))

    return list(options.values())[int(input("Elija su opcion:")) - 1]
