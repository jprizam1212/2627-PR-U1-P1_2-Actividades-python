def main():
    
    nombre = input("Introduce tu nombre: ")
    veces = int(input("Introduce un número entero: "))

    #esta linea lo que hace es repetir las lineas de su interior un cierto numero de veces 
    for _ in range(veces):
        print(nombre)


if __name__ == "__main__":
    main()