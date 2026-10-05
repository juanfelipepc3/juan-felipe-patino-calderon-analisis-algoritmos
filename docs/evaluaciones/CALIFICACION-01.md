# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Felipe Patiño Calderon · **Laboratorio:** Laboratorio 1 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `6e9c545`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (17 / 25)
**Lo que hizo bien:**
- Separa bien la corrección de la eficiencia y nombra la restricción que se incumple: la ventana de cuatro horas.
- En la Parte 2 relaciona el tiempo de ejecución con el consumo de energía y explica por qué se acumula al correr todas las madrugadas.
- Identifica dos perjuicios (el paciente y el operador del centro de contacto) y dice quién asume el costo de cada uno. También discute la obligación de que el orden de la lista sea siempre correcto.

**Lo que puede mejorar:**
- Dice que la ventana es "de 2 pm a 6 pm"; en el caso es de 2:00 a. m. a 6:00 a. m.
- No explica con claridad por qué duplicar la velocidad del servidor no resuelve el problema de fondo: solo dice que el algoritmo no escala linealmente. Falta decir que con un algoritmo cuadrático el tiempo seguiría creciendo mucho más rápido que la mejora del servidor.
- El segundo ejemplo (conciliación bancaria nocturna) es de su experiencia, pero no da cantidades (cuántas transacciones hay) ni la restricción exacta, así que queda general.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio sobre las entradas de un tamaño fijo, justifica que usaría el peor caso y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro verificando que se cumple el caso 2.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- El cálculo de insertion sort "línea a línea" es más una descripción por casos que un conteo: falta decir cuántas veces se ejecuta cada línea y sumar esos costos.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien (de mayor a menor), no alteran la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `sort()`. `merge_sort` tiene su propia mezcla recursiva.
- Los generadores producen lotes del tamaño pedido, sin repetidos y con semilla reproducible. El escenario B quedó bien armado (98 % ordenado y 2 % al final).
- Las funciones tienen docstring con el formato pedido.

**Lo que puede mejorar:**
- `medir_escenario` y `medir_algoritmo` no tienen tipo en el parámetro de la función recibida.
- Los archivos no terminan con una línea en blanco (aviso de estilo PEP 8) y los scripts no traen docstring al inicio del archivo.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados, leyenda y las curvas en los mismos ejes.
- Identifica con datos que C es el peor caso, B el mejor y A el promedio, y lo contrasta con su predicción.
- En la Parte 4 describe cómo crece cada curva, relaciona el factor de crecimiento (cerca de 4 contra cerca de 2) con las complejidades de 4.1 y explica por qué a n = 100 casi empatan.
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros (unas 5,6 horas para insertion sort, pocos segundos para merge sort), responde a la propuesta del servidor y menciona la memoria extra.

**Lo que puede mejorar:**
- Declare con claridad que las cifras de la extrapolación son una estimación con supuestos, no una medición, y cite la gráfica de donde sacó el dato.
- Los tiempos de la tabla de la Parte 4 (por ejemplo 0.575 s para n = 6400) no coinciden con lo que muestra la gráfica publicada (cerca de 0.48 s). Use los mismos datos en ambos.
- La conclusión sobre el servidor del doble de velocidad quedaría más sólida si indicara que el costo cuadrático lo supera en cuanto el volumen crezca.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- Ubicó el laboratorio en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con todos los archivos y las tres gráficas. Las gráficas se ven en el informe y la Parte 3 enlaza su código.
- Hay siete commits que tocan el laboratorio.

**Lo que puede mejorar:**
- No siguió la convención de nombres: el archivo se llama `Parte4_complejidad.py` (con P mayúscula) en vez de `parte4_complejidad.py`. Por eso el enlace de la Parte 4 del informe no abre el archivo en GitHub, donde las mayúsculas importan.
- El informe no trae instrucciones para reproducir los experimentos (cómo activar el entorno y qué comando ejecutar en cada parte).
- La Parte 4 no enlaza `algoritmos.py` ni `datos.py`; solo la Parte 3 lo hace.
- Varios mensajes de commit son poco descriptivos ("Corrección gráficas parte 3") y casi todo se subió el mismo día.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores y generan las gráficas. Ambos algoritmos ordenaron bien en mis pruebas con listas pequeñas y aleatorias, y el conteo de comparaciones es el esperado (por ejemplo, n − 1 en una lista ya en orden).

## Para el próximo laboratorio
- Nombre los archivos exactamente como pide el entregable y revise que los enlaces abran en GitHub.
- Agregue siempre una sección de instrucciones para reproducir los experimentos.
- Al calcular la complejidad línea a línea, escriba cuántas veces se ejecuta cada línea y sume.
- Dé cifras concretas en los ejemplos propios y explique con números por qué más hardware no reemplaza un mejor algoritmo.
- Haga commits más pequeños y con mensajes que digan qué cambió.
