def main():

    numero = int(input("Introduce un numro en segundos para pasar lo a a horas, minutos y segundos:  "))


    hora = numero // 3600

    minutos = (numero % 3600) // 60

    segundos = numero % 60

    print(f"{numero} segundos son {hora} horas, {minutos} minutos y {segundos} segundos.")


if __name__ == "__main__":
    main()  