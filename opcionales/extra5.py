def main():

    nombre = input("Nombre: ")
    primer_apellido = input("Primer apellido: ")
    segundo_apellido = input("Segundo apellido: ")
    año = input("Año: ")

    nombre = nombre[0:3].lower()
    primer_apellido = primer_apellido[0:3].lower()
    segundo_apellido = segundo_apellido[0:1].lower()
    año = año[2:4]

    print(f"Tu clave es: {nombre}{primer_apellido}{segundo_apellido}{año}")


if __name__ == "__main__":
    main()  