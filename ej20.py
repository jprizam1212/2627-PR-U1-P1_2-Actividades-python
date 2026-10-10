def main():
    
    telefono = input("Introduce el teléfono (+34-número-extensión): ")
   
    #divide en partes el telefono a partir del gion (-)
    partes = telefono.split("-")
   
    print(partes[1])


if __name__ == "__main__":
    main()