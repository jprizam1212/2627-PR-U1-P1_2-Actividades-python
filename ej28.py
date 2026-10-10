def main():
   
    a = float(input("Introduce el lado a: "))
    b = float(input("Introduce el lado b: "))
    c = float(input("Introduce el lado c: "))
    
    # Comprobar si las longitudes pueden formar un triángulo
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
       
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
       
        print(f"El área del triángulo es: {area:.2f}")
    
    else:
        print("Error: Las longitudes introducidas no pueden formar un triángulo.")

if __name__ == "__main__":
    main()