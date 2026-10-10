def main():

    nombre_completo = input("Escribe tu nombre completo y sepaa el nombre de los apellidos con una coma: ")

    partes = nombre_completo.split(",")

    nombre = partes[0]
    apellido = partes[1]

    print(f"{apellido} , {nombre}")
    
if __name__ == "__main__":
    main()    