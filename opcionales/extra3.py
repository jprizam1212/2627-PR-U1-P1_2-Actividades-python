def main():

    total = int(input("Introduce el número de días: "))

    semanas = total // 7 

    dias = total % 7 

    print(f"{total} dias equivalentes a: ")
    print(f"{semanas} semanas y {dias} dias")


if __name__ == "__main__":
    main() 