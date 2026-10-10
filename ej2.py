def main():

    horas = int(input("Horas de trabajo: "))
    coste = int(input("Coste por hora: ")) 

    suma = horas * coste 

    print(f"Importe total: {suma}")

if __name__ == "__main__":
    main()