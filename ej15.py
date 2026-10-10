def main():

    inversion = float(input("Introduce la cantidad depositada en la cuenta: "))

    #Calculo año 1
    anio1 = inversion * 1.04
    print(f"Balance tras el primer año: {round(anio1, 2)} €")

    #Calculo año 2
    anio2 = anio1 * 1.04
    print(f"Balance tras el segundo año: {round(anio2, 2)} €")

    #Calculo año 3
    anio3 = anio2 * 1.04
    print(f"Balance tras el tercer año: {round(anio3, 2)} €")


if __name__ == "__main__":
    main()