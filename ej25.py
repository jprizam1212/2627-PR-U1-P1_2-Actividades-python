def main():

    fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa):")

    #Esto hace que cada vez que halla una barra se divida 
    partes = fecha.split("/")

    dia = partes[0]
    mes = partes[1]
    año = partes[2]

    


if __name__ == "__main__":
    main()