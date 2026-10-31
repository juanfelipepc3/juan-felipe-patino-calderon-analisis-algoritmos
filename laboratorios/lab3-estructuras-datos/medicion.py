"""Medicion de tiempos de busqueda en lista enlazada y tabla hash.

Ejecute con:
    python medicion.py

Genera las graficas en graficas/lista_vs_tabla.png y graficas/tiempo_vs_alfa.png
"""

import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

# ---------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def primo_cercano(objetivo: int) -> int:
    """Devuelve un numero primo mayor o igual al objetivo.

    Args:
        objetivo: valor minimo deseado.

    Returns:
        El menor primo >= objetivo.
    """
    candidato = max(2, objetivo)
    while True:
        es_primo = True
        if candidato < 2:
            es_primo = False
        else:
            for d in range(2, int(candidato**0.5) + 1):
                if candidato % d == 0:
                    es_primo = False
                    break
        if es_primo:
            return candidato
        candidato += 1


# ---------------------------------------------------------------
# Experimento A — Lista frente a tabla
# ---------------------------------------------------------------

def experimento_a() -> None:
    """Mide el tiempo de busqueda de guias inexistentes en lista y tabla.

    Genera la grafica graficas/lista_vs_tabla.png.
    """
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    num_busquedas = 200
    repeticiones = 3  # repetir cada medicion y promediar

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    semilla_datos = 123

    for n in valores_n:
        print(f"  Experimento A: n = {n} ...")

        # Generar guias con semilla fija
        rng = random.Random(semilla_datos)
        guias = rng.sample(range(10**9, 10**10 - 1), n)
        estados = ["en bodega"] * n
        conjunto_guias = set(guias)

        # Construir las estructuras
        lista = ListaEnlazada()
        m = primo_cercano(n // 2)
        tabla = TablaHash(m)

        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        # Verificar que ambas devuelven lo mismo para una muestra
        muestra = guias[:min(10, n)]
        for guia in muestra:
            assert lista.buscar(guia) == tabla.buscar(guia), (
                f"Discrepancia en guia {guia}"
            )

        # Generar guias inexistentes
        inexistentes = generar_guias_inexistentes(conjunto_guias, num_busquedas)

        # Medir lista (promedio de varias repeticiones)
        t_lista_acum = 0.0
        for _ in range(repeticiones):
            inicio = time.perf_counter()
            for guia in inexistentes:
                lista.buscar(guia)
            fin = time.perf_counter()
            t_lista_acum += (fin - inicio)
        t_medio_lista = t_lista_acum / (repeticiones * num_busquedas)

        # Medir tabla (promedio de varias repeticiones)
        t_tabla_acum = 0.0
        for _ in range(repeticiones):
            inicio = time.perf_counter()
            for guia in inexistentes:
                tabla.buscar(guia)
            fin = time.perf_counter()
            t_tabla_acum += (fin - inicio)
        t_medio_tabla = t_tabla_acum / (repeticiones * num_busquedas)

        tiempos_lista.append(t_medio_lista * 1_000_000)  # a microsegundos
        tiempos_tabla.append(t_medio_tabla * 1_000_000)

        print(f"    m = {m}, alfa = {n/m:.2f}, "
              f"lista = {t_medio_lista*1e6:.2f} us, "
              f"tabla = {t_medio_tabla*1e6:.2f} us")

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos_lista, "o-", color="#e74c3c",
             linewidth=2, markersize=7, label="Lista enlazada")
    plt.plot(valores_n, tiempos_tabla, "s-", color="#2ecc71",
             linewidth=2, markersize=7, label="Tabla hash")
    plt.title("Tiempo medio de busqueda (guias inexistentes) vs n",
              fontsize=14, fontweight="bold")
    plt.xlabel("Numero de guias almacenadas (n)", fontsize=12)
    plt.ylabel("Tiempo medio por busqueda (microsegundos)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()
    print("  Grafica guardada en graficas/lista_vs_tabla.png")

    # Imprimir tabla de datos para el README
    print("\n  Datos del Experimento A:")
    print(f"  {'n':>8} | {'m':>8} | {'alfa':>6} | "
          f"{'Lista (us)':>12} | {'Tabla (us)':>12}")
    print(f"  {'-'*8}-+-{'-'*8}-+-{'-'*6}-+-{'-'*12}-+-{'-'*12}")
    for i, n in enumerate(valores_n):
        m = primo_cercano(n // 2)
        alfa = n / m
        print(f"  {n:>8} | {m:>8} | {alfa:>6.2f} | "
              f"{tiempos_lista[i]:>12.2f} | {tiempos_tabla[i]:>12.2f}")


# ---------------------------------------------------------------
# Experimento B — Efecto del factor de carga
# ---------------------------------------------------------------

def experimento_b() -> None:
    """Mide el tiempo de busqueda variando el factor de carga alfa.

    Con n = 20000 fijo, varia m para obtener distintos valores de alfa.
    Genera la grafica graficas/tiempo_vs_alfa.png.
    """
    n = 20000
    num_busquedas = 200
    repeticiones = 3

    # Valores objetivo de alfa y los m correspondientes (primos cercanos)
    alfas_objetivo = [0.25, 0.5, 1, 2, 4, 10]

    alfas_reales: list[float] = []
    tiempos: list[float] = []

    semilla_datos = 456
    rng = random.Random(semilla_datos)
    guias = rng.sample(range(10**9, 10**10 - 1), n)
    conjunto_guias = set(guias)
    inexistentes = generar_guias_inexistentes(conjunto_guias, num_busquedas)

    for alfa_obj in alfas_objetivo:
        m = primo_cercano(int(n / alfa_obj))
        alfa_real = n / m

        print(f"  Experimento B: alfa objetivo = {alfa_obj}, "
              f"m = {m}, alfa real = {alfa_real:.4f} ...")

        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en bodega")

        # Medir busquedas inexistentes
        t_acum = 0.0
        for _ in range(repeticiones):
            inicio = time.perf_counter()
            for guia in inexistentes:
                tabla.buscar(guia)
            fin = time.perf_counter()
            t_acum += (fin - inicio)
        t_medio = t_acum / (repeticiones * num_busquedas)

        alfas_reales.append(alfa_real)
        tiempos.append(t_medio * 1_000_000)

        print(f"    tiempo medio = {t_medio*1e6:.2f} us")

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(alfas_reales, tiempos, "D-", color="#3498db",
             linewidth=2, markersize=8, label="Tabla hash (n = 20 000)")
    plt.title("Tiempo medio de busqueda vs factor de carga (alfa)",
              fontsize=14, fontweight="bold")
    plt.xlabel("Factor de carga (alfa = n / m)", fontsize=12)
    plt.ylabel("Tiempo medio por busqueda (microsegundos)", fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()
    print("  Grafica guardada en graficas/tiempo_vs_alfa.png")

    # Imprimir tabla de datos para el README
    print("\n  Datos del Experimento B:")
    print(f"  {'alfa':>8} | {'m':>8} | {'Tiempo (us)':>12}")
    print(f"  {'-'*8}-+-{'-'*8}-+-{'-'*12}")
    for i in range(len(alfas_reales)):
        print(f"  {alfas_reales[i]:>8.4f} | "
              f"{primo_cercano(int(n / alfas_objetivo[i])):>8} | "
              f"{tiempos[i]:>12.2f}")


# ---------------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------------

if __name__ == "__main__":
    os.makedirs("graficas", exist_ok=True)

    print("=" * 60)
    print("Experimento A: Lista enlazada vs Tabla hash")
    print("=" * 60)
    experimento_a()

    print()
    print("=" * 60)
    print("Experimento B: Efecto del factor de carga")
    print("=" * 60)
    experimento_b()

    print()
    print("Mediciones completadas.")
