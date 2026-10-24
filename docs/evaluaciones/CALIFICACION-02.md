# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Juan Felipe Patiño Calderón · **Laboratorio:** Dividir y vencer (subarreglo máximo)
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `d95e961`

Muy buen trabajo: las dos soluciones funcionan y el informe es claro y apoyado en sus datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 20 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar desde n = 50 y explica por qué en n = 10 pierde (costo de las llamadas recursivas).
- En el máximo de un arreglo plantea `T(n) = 2T(n/2) + Θ(1)`, concluye `Θ(n)` y explica que dividir no aporta nada frente a un recorrido simple.
- Recomienda divide y vencerás y declara que lo de 1.000.000 de registros es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Los tiempos que usa en la estimación y en el punto de cruce salen de su tabla, que no coincide con lo que muestra la gráfica publicada (ver punto 4).

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde sale cada término y la resuelve con el método maestro (caso 2), concluyendo `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta por los dos ciclos anidados.

**Lo que puede mejorar:**
- Al aplicar el método maestro, escriba la comparación completa de `f(n)` con `n^(log_b a)` y diga explícitamente que la condición del caso 2 se cumple porque ambos son `Θ(n)`.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones de `subarreglo.py` son correctas, resuelven los tres casos, no llaman a la fuerza bruta y no modifican la lista.
- `pruebas.py` cubre todos los casos pedidos y las 20 listas aleatorias.
- `subarreglo.py` tiene type hints y docstrings.

**Lo que puede mejorar:**
- `medicion.py` no tiene docstrings ni type hints en su función.
- En `medicion.py` y `pruebas.py` faltan las dos líneas en blanco entre funciones (PEP 8). Además quedó un comentario de borrador ("Ah, wait...") en las pruebas.

## 4. Calidad del análisis de las gráficas (20 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calcula el factor al duplicar n (4000 a 8000) para ambos algoritmos y lo contrasta con `Θ(n²)` y `Θ(n log n)`.
- Incluye una tabla con los tiempos, útil porque los tamaños pequeños no se distinguen en la gráfica.

**Lo que puede mejorar:**
- La tabla del informe no coincide con la gráfica publicada: en la gráfica la fuerza bruta marca cerca de 0.72 s en n = 4000 y cerca de 2.6 s en n = 8000, y en la tabla dice 0.666 s y 2.724 s. Con la gráfica el factor sería cercano a 3.6, no 4.09. Las cifras del informe deben salir de la misma corrida que la gráfica.
- No indica si repitió las mediciones; repetirlas y promediar da datos más estables.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta `laboratorios/lab2-divide-y-vencer/` en la ubicación acordada, con todos los archivos del entregable.
- El informe sigue el orden pedido, enlaza el código en cada parte, tiene instrucciones de reproducción y la gráfica se ve.
- Seis commits descriptivos.

**Lo que puede mejorar:**
- Aunque los comandos de reproducción funcionan, indique que `pruebas.py` y `medicion.py` también pueden correrse desde la carpeta del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en listas aleatorias y la medición corre completa y genera la gráfica.

## Para el próximo laboratorio
- Copie en el informe los valores de la misma corrida que produjo la gráfica publicada.
- Agregue docstrings y type hints a todas las funciones, también las de medición.
- Deje dos líneas en blanco entre funciones en todos los archivos antes de subir.
- Repita cada medición varias veces y diga en el informe que lo hizo.
- Verifique en el método maestro la condición del caso paso a paso.
