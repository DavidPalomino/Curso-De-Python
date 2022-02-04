Elije = input("Que moneda quieres volver dolares: Soles , Pesos Colombianos o Pesos Mexicanos? ")
Elije = str(Elije)
print(Elije)
if Elije == "Soles":
    Soles = input("Cuantos Soles Tienes? :")
    Soles = float(Soles)
    valor_dolar_peru = 3.86
    dolar_peru = Soles / valor_dolar_peru
    dolar_peru = round(dolar_peru, 2)
    dolar_peru = str(dolar_peru)
    print("Tienes $" + dolar_peru + " dolares")
elif Elije == "Pesos Colombianos":
    pesos = input("Cuantos pesos colombianos tienes? :")
    pesos = float(pesos)
    valor_dolar_colombia = 3875
    dolares_colombia = pesos / valor_dolar_colombia
    dolares_colombia = round(dolares_colombia, 2)
    dolares_colombia = str(dolares_colombia)
    print("Tienes $" + dolares_colombia + " dolares")
elif Elije == "Pesos Mexicanos" :
    pesos_mexicanos = input("Cuantos Pesos Mexicanos Tienes? ")
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar_mexico = 0.048
    dolar_mexico = pesos_mexicanos / valor_dolar_mexico
    dolar_mexico = round(dolar_mexico, 2)
    dolar_mexico = str(dolar_mexico)
    print("Tienes $" + dolar_mexico + "Dolares")
