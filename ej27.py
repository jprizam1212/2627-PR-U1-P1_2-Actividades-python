def main():
   
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio unitario del producto: "))
    unidades = int(input("Introduce el número de unidades: "))
    
    coste_total = precio * unidades

    #Esos numeros que hay es para el ancho de los numeros, la d del :3d es formato decimal
    print(f"{nombre}: {precio:09.2f} € | {unidades:03d} unidades | Total: {coste_total:011.2f} €")

if __name__ == "__main__":
    main()