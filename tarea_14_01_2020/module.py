def read(archivo):
    '''La funcion read lee el triangulo, elimina los caracteres de linea nueva
    y lo separa por los espacios en blanco '''
    return [line.rstrip('\n').split(' ') for line in open(archivo, 'r')]


def loops(tri):
    ''' El argumento tri es la lista de numeros de cada linea del archivo,
    la funcion loop, revisa la pos x y la pos x + 1 y realiza la comparacion
    luego suma al arreglo pos y es lo que retorna, la suma de las vias mas larga '''
    pos = [0, 0]
    for num in range(len(tri)):
        pos[0] += int(tri[num][pos[1]])
        try:
            if int(tri[num + 1][pos[1]]) > int(tri[num + 1][pos[1] + 1]):
                pos[1] += 1
        except IndexError:
            pass
    return print(pos[0])
