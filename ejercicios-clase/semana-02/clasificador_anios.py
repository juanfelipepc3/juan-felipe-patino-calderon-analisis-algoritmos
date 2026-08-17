"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.

Incluye las extensiones sugeridas (bonus):
    - Agrupacion de anios por decada usando comprension de diccionario.
    - Validacion de anios negativos con try/except y mensaje propio.
    - Calculo del promedio de los anios bisiestos con el modulo statistics.
"""

import statistics


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas). También
    reintenta si algún año ingresado es negativo.

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2000,2023,2024): ")
        partes = [parte.strip() for parte in entrada.split(",") if parte.strip()]
        try:
            anios = [int(parte) for parte in partes]
            for anio in anios:
                if anio < 0:
                    raise ValueError(f"El año {anio} es negativo; solo se aceptan años positivos.")
            return anios
        except ValueError as error:
            print(f"Entrada inválida: {error}")
            print("Asegúrese de ingresar solo números enteros positivos separados por comas.")


def agrupar_por_decada(anios: list[int]) -> dict[int, list[int]]:
    """Agrupa una lista de años por su década de pertenencia.

    Por ejemplo, 2024 pertenece a la década 2020, y 1900 a la década 1900.

    Args:
        anios: lista de años a agrupar.

    Returns:
        Diccionario donde cada clave es una década (por ejemplo 2020) y
        cada valor es la lista de años de esa década (por ejemplo [2024]).
    """
    decadas = {anio // 10 * 10 for anio in anios}
    return {
        decada: [anio for anio in anios if anio // 10 * 10 == decada]
        for decada in sorted(decadas)
    }


def promedio_bisiestos(anios_bisiestos: list[int]) -> float | None:
    """Calcula el promedio de una lista de años bisiestos.

    Args:
        anios_bisiestos: lista de años bisiestos.

    Returns:
        El promedio como flotante, o None si la lista está vacía.
    """
    if not anios_bisiestos:
        return None
    return statistics.mean(anios_bisiestos)


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    anios_bisiestos = [anio for anio in anios if es_bisiesto(anio)]
    por_decada = agrupar_por_decada(anios)
    promedio = promedio_bisiestos(anios_bisiestos)

    print()
    print(f"Años ingresados: {anios}")
    print(f"Años bisiestos: {anios_bisiestos}")
    print(f"Cantidad de años bisiestos: {len(anios_bisiestos)} de {len(anios)}")
    print(f"Años agrupados por década: {por_decada}")

    if promedio is not None:
        print(f"Promedio de los años bisiestos: {promedio:.2f}")
    else:
        print("Promedio de los años bisiestos: no hay años bisiestos para calcular el promedio.")


if __name__ == "__main__":
    main()