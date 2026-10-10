import time
import random
import os
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def medir_tiempos():
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempos_fb = []
    tiempos_dv = []

    random.seed(42)

    for n in tamanos:
        # Generar datos
        valores = [random.randint(-100, 100) for _ in range(n)]

        # Medir fuerza bruta
        inicio_fb = time.perf_counter()
        fb_resultado = subarreglo_fuerza_bruta(valores)
        fin_fb = time.perf_counter()
        tiempo_fb = fin_fb - inicio_fb
        tiempos_fb.append(tiempo_fb)

        # Medir divide y vencerás
        inicio_dv = time.perf_counter()
        dv_resultado = subarreglo_maximo(valores, 0, n - 1)
        fin_dv = time.perf_counter()
        tiempo_dv = fin_dv - inicio_dv
        tiempos_dv.append(tiempo_dv)

        # Verificar que ambos algoritmos devuelven la misma suma
        assert fb_resultado[2] == dv_resultado[2], f"Diferencia en suma para n={n}. FB: {fb_resultado[2]}, DV: {dv_resultado[2]}"
        print(f"Tamaño: {n:4} | FB: {tiempo_fb:.6f} s | DV: {tiempo_dv:.6f} s")

    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, marker='o', label='Fuerza Bruta')
    plt.plot(tamanos, tiempos_dv, marker='x', label='Divide y Vencerás')
    plt.title('Tiempo de ejecución vs. Tamaño de entrada')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)

    # Guardar gráfica
    os.makedirs('graficas', exist_ok=True)
    plt.savefig('graficas/tiempo_vs_n.png')
    print("Gráfica guardada en graficas/tiempo_vs_n.png")

if __name__ == "__main__":
    medir_tiempos()
