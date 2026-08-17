def calcular_promedio(numeros: list[int]) -> float:
    """Calcula el promedio de una lista de numeros.

    Args:
        numeros: lista de numeros (enteros o flotantes) a promediar.

    Returns:
        El promedio de los numeros como valor flotante.
    """
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma / len(numeros)


def main() -> None:
    """Punto de entrada del script."""
    lista_ejemplo = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista_ejemplo)
    print(promedio)


if __name__ == "__main__":
    main()