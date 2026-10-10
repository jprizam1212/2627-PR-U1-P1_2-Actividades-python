def main():

    precio_original = float(input("Cual es el precio original: "))
    porcentaje_descuento = int(input("Cual es el procentaje de descuento: "))

    descuento = precio_original * (porcentaje_descuento / 100)

    precio_rebajado = precio_original - descuento

    iva = precio_rebajado * 0.21

    precio_final = precio_rebajado + iva

    print(f"El precio original es: {precio_original}")
    print(f"El descuento aplicado: {descuento}")
    print(f"El precio después del descuento: {precio_rebajado}")
    print(f"El IVA: {iva}")
    print(f"El precio final es: {precio_final}")
    

if __name__ == "__main__":
    main()