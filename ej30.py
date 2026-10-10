def main():
    
    numero = int(input("Introduce un número entero: "))
    
    # El 0, el 1 y los negativos no son primos
    if numero <= 1:
        print(f"El número {numero} NO es primo.")
    else:
        es_primo = True
        
        # Probamos a dividir el número entre todos los números desde el 2 hasta antes de él mismo
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(f"El número {numero} ES primo.")
        else:
            print(f"El número {numero} NO es primo.")

if __name__ == "__main__":
    main()