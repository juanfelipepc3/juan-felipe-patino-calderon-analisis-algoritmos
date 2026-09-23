"""Experimento de la Parte 4: validacion experimental de la complejidad.

Compara el tiempo de ejecucion de insertion_sort y merge_sort sobre el
escenario A (aleatorio) de Tamiza, para los mismos tamanos de entrada
de la Parte 3, y genera la grafica parte4_tiempo.png.
"""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir_algoritmo(funcion_ordenar, tamanos: list[int]) -> list[float]:
    """Mide el tiempo de ejecucion de un algoritmo sobre el escenario A.

    Para cada tamano, genera el lote aleatorio una sola vez (con
    semilla fija) y ejecuta el algoritmo REPETICIONES veces sobre ese
    mismo lote, reportando el tiempo promedio. Solo se cronometra la
    llamada al algoritmo, no la generacion de los datos.

    Args:
        funcion_ordenar: funcion de ordenamiento a medir (insertion_sort
            o merge_sort).
        tamanos: lista de tamanos de entrada a medir.

    Returns:
        Lista de tiempos promedio (en segundos), uno por cada tamano.
    """
    tiempos = []

    for n in tamanos:
        datos = generar_aleatorio(n)

        tiempos_repeticion = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            funcion_ordenar(datos)
            fin = time.perf_counter()
            tiempos_repeticion.append(fin - inicio)

        tiempo_promedio = sum(tiempos_repeticion) / len(tiempos_repeticion)
        tiempos.append(tiempo_promedio)
        print(f"  n={n:>5}  tiempo_prom={tiempo_promedio:.6f}s")

    return tiempos


def graficar_comparacion(resultados: dict[str, list[float]]) -> None:
    """Genera la grafica comparativa de tiempo vs. tamano de entrada.

    Args:
        resultados: diccionario con el nombre de cada algoritmo y su
            lista de tiempos por tamano.
    """
    plt.figure(figsize=(8, 5))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)

    plt.title("Insertion sort vs. merge sort: tiempo vs. tamaño de entrada (escenario A)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada del experimento de la Parte 4."""
    resultados: dict[str, list[float]] = {}

    for nombre, funcion_ordenar in ALGORITMOS.items():
        print(f"Midiendo: {nombre}")
        resultados[nombre] = medir_algoritmo(funcion_ordenar, TAMANOS)
        print()

    graficar_comparacion(resultados)
    print("Gráfica generada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()