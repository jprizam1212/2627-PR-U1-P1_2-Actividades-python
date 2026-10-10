def main():
    
    precio_regular = 3.49
    descuento = 0.60

    barras = int(input("Introduce el número de barras no frescas vendidas: "))

    #Calculos para saber el precio de las barras descontadas y de el conte total
    precio_con_descuento = precio_regular * (1 - descuento)
    coste_total = barras * descuento

    print(f"Precio habitual de una barra: {precio_regular} €")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Coste final total: {round(coste_total, 2)} €")


if __name__ == "__main__":
    main()