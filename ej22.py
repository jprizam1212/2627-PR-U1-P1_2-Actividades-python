def main():
    
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")

    #Busca la vocal en la frase que has indtroducido 
    resultado = frase.replace(vocal, vocal.upper())
    
    print(resultado)


if __name__ == "__main__":
    main()