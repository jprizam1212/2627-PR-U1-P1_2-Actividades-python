def main():
    ancho = 17
    alto = 12.0

    #Calculo
    suma1 = ancho / 2
    suma2 = ancho // 2
    suma3 = alto / 3
    suma4 = 1 + 2 * 5

    #typo   prueba = tipo1.split("-")
    tipo1 = type(suma1).__name__
    tipo2 = type(suma2).__name__
    tipo3 = type(suma3).__name__
    tipo4 = type(suma4).__name__

    print(f"1. {ancho} / 2 = {suma1}       |  El tipo del resultado es {tipo1}")   

    print(f"2. {ancho} // 2 = {suma2}       |  El tipo del resultado es {tipo2} ")

    print(f"3. {alto} / 3 = {suma3}       |  El tipo del resultado es {tipo3}")

    print(f"4. 1 + 2 * 5 = {suma4}       |  El tipo del resultado es {tipo4} ")


if __name__ == "__main__":
    main()