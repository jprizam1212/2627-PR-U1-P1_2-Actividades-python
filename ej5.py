def main():

    precio_sin_iva = int(input("Cual es el precio sin IVA: "))

    precio_con_iva = precio_sin_iva * 1.21

    print(f"El precio con el IVA incluido es: {precio_con_iva}")


if __name__ == "__main__":
    main()