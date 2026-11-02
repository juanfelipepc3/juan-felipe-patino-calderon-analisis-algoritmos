# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Juan Felipe Patiño Calderón · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `9c2788f`

Muy buen trabajo en general.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explicó bien la colisión con el ejemplo de las guías 10, 24 y 17 con m = 7, y comparó encadenamiento con direccionamiento abierto, con ventajas y costos.
- Justificó que la tabla hash no sirve para rangos porque pierde el orden de las claves.
- Recomendó tabla hash más árbol equilibrado y dio una estimación a 5.000.000 de envíos, declarada como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el árbol degenerado dio la altura y el costo de una sola búsqueda, pero no el número total de comparaciones al insertar las 400.000 guías una a una.
  → *Cómo corregirlo:* piense cuántos nodos hay que recorrer en cada inserción cuando el árbol ya es una cadena, y sume ese costo sobre todas las guías.
- La estimación de la tabla ("menos de 1 μs") se apoya en que nunca pasó de 1 μs, sin explicar mejor por qué la curva seguiría plana.
  → *Cómo corregirlo:* relacione la estimación con el valor de α que mantendría y con el comportamiento de su primera gráfica.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justificó el Θ(n) de la lista y el Θ(1 + α) de la tabla, nombró el hash uniforme simple y explicó que si todo cae en una casilla la tabla vuelve a Θ(n).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- La lista y la tabla funcionan, la colisión forzada con m = 7 pasa, `factor_carga` da 3/7 y las veinte colecciones aleatorias coinciden.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`. Hay type hints y docstrings con `Args` y `Returns`.

**Lo que puede mejorar (y cómo corregirlo):**
- La verificación de coincidencia en `medicion.py` solo usa guías existentes y no revisa inexistentes.
  → *Cómo corregirlo:* añada una comprobación sobre unas pocas guías inexistentes.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera tiene seis valores de n y la segunda seis valores de α.
- Calculó el factor de crecimiento de la lista (≈ 4.33 frente a 4 de n) y lo contrastó con Θ(n); los valores del informe coinciden con la gráfica.

**Lo que puede mejorar (y cómo corregirlo):**
- En la segunda gráfica el tiempo baja de α = 1 a α = 2 y 4, y solo sube hacia α = 10. Eso no muestra claramente Θ(1 + α), y lo atribuyó al ruido sin comprobarlo.
  → *Cómo corregirlo:* repita la medición más veces o con más búsquedas por punto, y calcule un factor de crecimiento entre dos valores de α, como hizo con n.
- Para la tabla no calculó un factor de crecimiento entre n consecutivos, solo comparó dos valores sueltos.
  → *Cómo corregirlo:* divida el tiempo de la tabla en dos n consecutivos y compare ese cociente con el de la lista.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura acordada (`laboratorios/lab3-estructuras-datos/`), el informe tiene el orden pedido, las imágenes se ven con ruta relativa y cada parte enlaza su código.
- Hay instrucciones de reproducción y tres commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa y genera las dos gráficas.
