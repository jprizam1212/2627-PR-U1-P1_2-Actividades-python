def main():

    hora = int(input("Hora de comienzo: "))
    minutos = int(input("Minuto de comienzo: "))
    duracion = int(input("Duracion: "))

    #Juntamos todos los minutos para luego restarle la duracion 
    minuto_totales_inicio = (hora * 60) + minutos
    minuto_totales_final = minuto_totales_inicio + duracion

    #Luego solo tenemos que dividir esas horas totales y tendremos el resultado
    hora_fin = (minuto_totales_final // 60 ) % 24
    minutos_fin =minuto_totales_final % 60

    print(f"La película termina a las {hora_fin}:{minutos_fin}")


if __name__ == "__main__":
    main() 