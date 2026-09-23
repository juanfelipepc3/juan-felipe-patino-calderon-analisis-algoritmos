import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def medir_escenario(generador, tamanos: list[int]) -> tuple[list[float], list[int]]:
    """Mide tiempo y comparaciones de insertion_sort para un generador.

    Para cada tamano, genera el lote una sola vez y ejecuta
    insertion_sort REPETICIONES veces, reportando el tiempo promedio.
    El numero de comparaciones es deterministico para un mismo lote,
    asi que se toma de una sola ejecucion.

    Args:
        generador: funcion generadora del escenario (recibe n y
            devuelve una lista de enteros).
        tamanos: lista de tamanos de entrada a medir.

    Returns:
        Una tupla con la lista de tiempos promedio (en segundos) y la
        lista de numero de comparaciones, una por cada tamano.
    """
    tiempos = []
    comparaciones_totales = []

    for n in tamanos:
        datos = generador(n)

        tiempos_repeticion = []
        comparaciones = 0
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, comparaciones = insertion_sort(datos)
            fin = time.perf_counter()
            tiempos_repeticion.append(fin - inicio)

        tiempo_promedio = sum(tiempos_repeticion) / len(tiempos_repeticion)
        tiempos.append(tiempo_promedio)
        comparaciones_totales.append(comparaciones)

        print(f"  n={n:>5}  tiempo_prom={tiempo_promedio:.6f}s  comparaciones={comparaciones}")

    return tiempos, comparaciones_totales


def graficar_comparaciones(resultados: dict[str, list[int]]) -> None:
    """Genera la grafica de comparaciones vs. tamano de entrada.

    Args:
        resultados: diccionario con el nombre de cada escenario y su
            lista de comparaciones por tamano.
    """
    plt.figure(figsize=(8, 5))
    for nombre, comparaciones in resultados.items():
        plt.plot(TAMANOS, comparaciones, marker="o", label=nombre)

    plt.title("Insertion sort: comparaciones vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png", dpi=150)
    plt.close()


def graficar_tiempo(resultados: dict[str, list[float]]) -> None:
    """Genera la grafica de tiempo vs. tamano de entrada.

    Args:
        resultados: diccionario con el nombre de cada escenario y su
            lista de tiempos por tamano.
    """
    plt.figure(figsize=(8, 5))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)

    plt.title("Insertion sort: tiempo de ejecución vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada del experimento de la Parte 3."""
    tiempos_por_escenario: dict[str, list[float]] = {}
    comparaciones_por_escenario: dict[str, list[int]] = {}

    for nombre, generador in ESCENARIOS.items():
        print(f"Midiendo escenario: {nombre}")
        tiempos, comparaciones = medir_escenario(generador, TAMANOS)
        tiempos_por_escenario[nombre] = tiempos
        comparaciones_por_escenario[nombre] = comparaciones
        print()

    graficar_comparaciones(comparaciones_por_escenario)
    graficar_tiempo(tiempos_por_escenario)
    print("Gráficas generadas en graficas/parte3_comparaciones.png y graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()