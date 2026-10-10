def main():
   
    limite = int(input("Introduce el valor máximo hasta el que quieres calcular Fibonacci: "))
    
    # Los dos primeros números de la serie
    num1 = 0
    num2 = 1
    
    print(f"Secuencia de Fibonacci hasta {limite}:")
    
    # while = mientras de seudocodigo
    while num1 <= limite:
        print(num1)
        
        siguiente = num1 + num2
        
        num1 = num2
        num2 = siguiente

if __name__ == "__main__":
    main()