def main():

    importe_final = float(input("Introduce el importe final del alticulo: ")) 

    importe_sin_iva = importe_final / 1.10

    iva_pagado = importe_final - importe_sin_iva

    #los :.2f significan que queremos que se vean 2 decimales y la f que sean tipo float
    print(f"Importe sin IVA: {importe_sin_iva:.2f} €")
    print(f"IVA pagado (10%): {iva_pagado:.2f} €")

if __name__ == "__main__":
    main()