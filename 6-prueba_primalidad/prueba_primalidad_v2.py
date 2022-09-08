def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n - 1)
    return resultado


def es_primo(numero):
    return (factorial(numero -1) + 1) % numero == 0


def run():
    numero = int(input('Ingresa un numero: '))
    if es_primo(numero):
        print('Es un numero primo')
    else:
        print('No es un numero primo')


if __name__ == '__main__':
    run()