
def obtener_latitud(coordenada: str) -> float:
    """

    """
    pos_coma: int = coordenada.find(",")

    return float(coordenada[0:pos_coma])


def obtener_longitud(coordenada: str) -> float:
    """

    """
    pos_coma: int = coordenada.find(",")

    return float(coordenada[pos_coma + 1:])


def main():
    coordenada = input("Introduce las coordenadas: ")

    latitud = obtener_latitud(coordenada)
    longitud = obtener_longitud(coordenada)

    print(f"Latitud:{latitud}")
    print(f"Longitud:{longitud}")


if __name__ == "__main__":
    main()