# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiento a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1, 2, 3): '))
msg = 'Elegiste la opción '
if opcion == 1:
    conversacion(msg + str(opcion))
elif opcion == 2:
    conversacion(msg + str(opcion))
elif opcion == 3:
    conversacion(msg + str(opcion))
else:
    print('Escribe la opción correcta')