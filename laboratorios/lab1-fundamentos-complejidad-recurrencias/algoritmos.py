"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    # Se ordena de mayor a menor (convencion de Tamiza: el paciente de
    # mayor riesgo queda primero). Por eso se desplazan los elementos
    # MENORES que la clave, en vez de los mayores.
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] < clave:
            comparaciones += 1
            lista[j + 1] = lista[j]
            j -= 1
        if j >= 0:
            comparaciones += 1
        lista[j + 1] = clave

    return lista, comparaciones


def _mezclar(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos sublistas ya ordenadas de mayor a menor en una sola.

    Args:
        izquierda: sublista ya ordenada de mayor a menor.
        derecha: sublista ya ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada (ordenada de mayor a menor) y
        el numero de comparaciones entre elementos realizadas al
        mezclar.
    """
    resultado = []
    comparaciones = 0
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Los elementos restantes ya estan ordenados entre si: copiarlos
    # no implica ninguna comparacion adicional entre elementos.
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    medio = len(datos) // 2
    izquierda, comparaciones_izq = merge_sort(datos[:medio])
    derecha, comparaciones_der = merge_sort(datos[medio:])
    combinada, comparaciones_mezcla = _mezclar(izquierda, derecha)

    total_comparaciones = comparaciones_izq + comparaciones_der + comparaciones_mezcla
    return combinada, total_comparaciones