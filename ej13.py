def main():

    num1 = int(input("Escribe un numero que quieras dividir: "))
    divisor = int(input("Escribe entre cuanto quieres dividirlo: "))

    if divisor == 0:
        print("Entre 0 no se puede dividir prueba otro numero")
        divisor = int(input("Escribe entre cuanto quieres dividirlo: "))
    else:

        #Calculo cociente
        cociente = num1 // divisor

        #Calculo resto
        resto = num1 % divisor

        print(f"La división de {num1} entre {divisor} da un cociente {cociente} y un resto {resto}")

if __name__ == "__main__":
    main()