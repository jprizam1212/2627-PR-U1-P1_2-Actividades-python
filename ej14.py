def main():

    payasos = int(input("Cuantos payasos se han vendido: "))
    muñecas = int(input("Cuantas muñecas se han vendido: "))

    #para saber el peso de cad apayaso y muñeco multiplicamos el numero que se han vendido por el peso de uno solo 
    peso_payasos = payasos * 112
    peso_muñecas = muñecas * 75

    #para saber el peso total solo hay que sumar hambas partes 
    suma = peso_payasos + peso_muñecas

    print(f"El peso total de los payasos es {peso_payasos} y el peso tatal de muñecas es {peso_muñecas}")
    print(f"El peso total es {suma}")

if __name__ == "__main__":
    main()