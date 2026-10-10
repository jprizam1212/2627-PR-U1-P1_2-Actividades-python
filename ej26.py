def main():

    cesta = input("Introduce tu compra separando los productos por comas: ")

    #Esto hace que cada vez que halla una coma se divida 
    producto = cesta.split(",")

    for producto in producto:
        print(producto)


if __name__ == "__main__":
    main()