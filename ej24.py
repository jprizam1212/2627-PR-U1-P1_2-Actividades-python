def main():

    precio = input("Introduce el precio del producto en euros (con dos decimales):")

    parte = precio.split(".")

    #La primera partes sempre es 0 y se va sumando rogresivamente
    euros = parte[0]
    centimos = parte[1]

    print("Número de euros:", euros)
    print("Número de céntimos:", centimos)

if __name__ == "__main__":
    main()