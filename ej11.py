def main():

    num1 = int(input("Introduce un numero: "))

    #en esta formula tambien es muy importante poner bien los parentesis
    suma = ( (num1 * (num1 + 1)) / 2)

    print(f"Esta es la suma de todos los numeros enteros desde 1 hasta {num1}: {suma}")

if __name__ == "__main__":
    main()