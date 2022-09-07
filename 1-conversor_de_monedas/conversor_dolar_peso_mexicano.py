dolares = float(input("¿Cuántos dólares tienes?: "))
valor_peso = 0.050
pesos = str(round(dolares / valor_peso, 2))
print("Tienes $" + pesos + "pesos méxicanos")