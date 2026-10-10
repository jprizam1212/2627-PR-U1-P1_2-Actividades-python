def main():
    
    numero = int(input("Escribe un numero "))

    print (f"Los divisores de {numero} son: ")

    for contador in range(1, numero + 1): 
        if numero % contador == 0:
            print (contador)

if __name__ == "__main__":
    main()