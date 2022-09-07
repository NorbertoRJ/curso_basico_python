peso_mexicano = float(input("¿Cuántos pesos méxicanos tienes tienes?: "))
valor_dolar = 19.97
dolares = str(round(peso_mexicano / valor_dolar, 2))
print("Tienes $" + dolares + " dólares")