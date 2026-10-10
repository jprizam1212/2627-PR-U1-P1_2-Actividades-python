def main():

    import random  
    
    minimo = int(input("Introduce el valor mínimo: "))
    maximo = int(input("Introduce el valor máximo: "))
    
    numero_aleatorio = random.randint(minimo, maximo)
    
    print(f"El número aleatorio entre {minimo} y {maximo} es: {numero_aleatorio}")

if __name__ == "__main__":
    main()