def main():
    
    celsius = int(input("Que temperatura hace (grados celsius): "))
    
    #Calcular los grados fahrenheit
    
    fahrenheit = ( celsius * 9 / 5) + 32 

    print(f"La temperatura pasada a fahrenheit es: {fahrenheit}")
if __name__ == "__main__":
    main()