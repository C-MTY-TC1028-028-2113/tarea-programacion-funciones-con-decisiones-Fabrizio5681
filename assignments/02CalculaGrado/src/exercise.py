def calcula_grado(grado1):
    if grado1 < 0.0 or grado1 > 1.0:
        nota = "score incorrecto"
    elif grado1 > 0.9:
        nota = "A"
    elif grado1 > 0.8:
        nota = "B"
    elif grado1 > 0.7:
        nota = "C"
    elif grado1 > 0.6:
        nota = "D"
    else:
        nota = "F"
    return nota


def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
