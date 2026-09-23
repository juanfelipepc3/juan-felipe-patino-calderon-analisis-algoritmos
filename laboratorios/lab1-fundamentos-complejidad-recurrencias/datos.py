import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    generador = random.Random(semilla)
    indices = list(range(1, n + 1))
    generador.shuffle(indices)
    return indices


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    generador = random.Random(semilla)

    tamano_ordenado = int(n * 0.98)
    tamano_nuevo = n - tamano_ordenado

    # Los indices mas altos forman la parte ya ordenada de mayor a
    # menor, generados directamente en ese sentido (sin invocar
    # ninguna funcion de ordenamiento).
    parte_ordenada = list(range(n, tamano_nuevo, -1))

    # Los indices restantes (los mas bajos) son los registros nuevos
    # del dia, que llegan sin ordenar al final del lote.
    parte_nueva = list(range(1, tamano_nuevo + 1))
    generador.shuffle(parte_nueva)

    return parte_ordenada + parte_nueva


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(1, n + 1))