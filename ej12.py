def main():

    peso = float(input("Cuanto pesas: "))
    altura = float(input("Cuanto mides: ")) 

    masa_total = peso / (altura ** 2)

    #El comando round sirve para redondear el resultado (por si sale muy grande)
    masa_total = round(masa_total, 2)

    print(f"Tu masa corporal total es de: {masa_total}")   

if __name__ == "__main__":
    main()