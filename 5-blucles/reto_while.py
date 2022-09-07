#usar break y continue con while
def usando_break():
    contador = -1
    while contador < 1000:
        contador += 1
        if contador % 2 == 0:
            continue
        print(str(contador) + ' es un número impar')


def usando_continue():
    contador = 0
    while contador < 100000:
        print(contador)
        if contador == 543:
            break
        contador += 1


def run():
    menu = """
    1 - usando break
    2 - usando continue

    Elige una opción: """

    opcion = int(input(menu))
    if opcion == 1:
        usando_break()
    elif opcion == 2:
        usando_continue()
    else:
        print('Selecciona una opción correcta')


if __name__ == '__main__':
    run()