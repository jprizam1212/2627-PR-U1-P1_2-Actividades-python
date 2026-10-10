def main():
    
    email = input("Introduce tu correo electrónico: ")
    
    nombre_usuario = email.split("@")[0]

    #Coge una parte de la que dividimos antes y lo repite poniendo al final el resultado de la suma 
    nuevo_email = nombre_usuario + "@ceu.es"
    
    print("Tu nuevo correo electrónico es:", nuevo_email)


if __name__ == "__main__":
    main()