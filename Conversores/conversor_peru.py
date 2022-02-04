soles = input("Cuantos Soles Tienes? :")
soles = float(soles)
valor_dolar = 3.86
dolar = soles / valor_dolar
dolar = round(dolar, 2)
dolar = str(dolar)
print("Tienes $" + dolar + " dolares")