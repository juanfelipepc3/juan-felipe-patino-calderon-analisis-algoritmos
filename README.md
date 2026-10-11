# Curso de Análisis de Algoritmos

Repositorio para los laboratorios y ejercicios prácticos del curso de Análisis de Algoritmos.

## Estructura del repositorio

- `laboratorios/`: informes de laboratorio evaluativos, uno por carpeta.
- `ejercicios-clase/`: ejercicios de las sesiones prácticas no evaluativas.
- `benchmarks/`: scripts compartidos de medición de tiempos y graficación.

## Cómo clonar este repositorio
```bash
git clone https://github.com/juanfelipepc3/juan-felipe-patino-analisis-algoritmos.git
```

## Autor

Juan Felipe Patiño Calderón

## Comandos útiles

### Navegación en la terminal

```bash
pwd                 # muestra la carpeta actual
ls                   # lista archivos y carpetas (dir en cmd de Windows)
cd nombre-carpeta    # entra a una carpeta
cd ..                # sube un nivel
mkdir nombre-carpeta # crea una carpeta nueva
```

### Flujo básico de Git

```bash
git status                    # ver qué archivos cambiaron
git add archivo.py            # preparar un archivo para el commit
git add .                     # preparar todos los cambios
git commit -m "mensaje"       # guardar los cambios preparados
git push                      # subir los commits a GitHub
git pull                      # traer cambios desde GitHub
git log --oneline             # ver el historial de commits
```

# Semana 02 — Configuración del entorno de trabajo

Esta carpeta contiene el entorno virtual y los scripts de la sesión práctica de la Semana 2.

## Cómo se creó el entorno virtual

```bash
python3 -m venv venv
```

## Cómo se activó

```bash
source venv/bin/activate     # Git Bash / Mac / Linux
venv\Scripts\activate        # Windows (cmd / PowerShell)
```

Se verificó el prefijo `(venv)` en la terminal antes de instalar cualquier dependencia.

## Cómo reproducir este entorno en otra máquina

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Esto instala exactamente las mismas versiones de las librerías usadas en este proyecto (`matplotlib`), listadas en `requirements.txt`.

## Contenido de la carpeta

- `requirements.txt`: dependencias del proyecto, generadas con `pip freeze`.
- `refactor_pep8.py`: script de la Parte 3, refactorizado siguiendo PEP 8.
- `clasificador_anios.py`: ejercicio integrador de la Parte 4 (clasificador de años bisiestos).

---

## Laboratorios Implementados

### [Laboratorio 1: Fundamentos, Complejidad y Recurrencias](laboratorios/lab1-fundamentos-complejidad-recurrencias/)
- **Ubicación:** `laboratorios/lab1-fundamentos-complejidad-recurrencias/`
- **Descripción:** Análisis de la complejidad de algoritmos básicos y resolución empírica/matemática de relaciones de recurrencia, evaluando distintos escenarios:
  1. **Análisis de casos:** Comparación empírica del desempeño algorítmico en su mejor caso, caso promedio y peor caso.
  2. **Órdenes de crecimiento:** Demostración práctica del comportamiento asintótico para diferentes clases de complejidad (ej. lineal, cuadrática).
- **Entregables:** Incluye implementaciones de algoritmos y utilidades de datos (`algoritmos.py`, `datos.py`), scripts experimentales para medición (`parte3_casos.py`, `Parte4_complejidad.py`), gráficas de rendimiento y un informe resolviendo ecuaciones de recurrencia.

### [Laboratorio 2: Divide y Vencerás (Subarreglo Máximo)](laboratorios/lab2-divide-y-vencer/)
- **Ubicación:** `laboratorios/lab2-divide-y-vencer/`
- **Descripción:** Solución al problema del subarreglo máximo (máxima variación de caja consecutiva) comparando dos enfoques:
  1. **Fuerza Bruta:** con complejidad asintótica $\Theta(n^2)$.
  2. **Divide y Vencerás:** resolviendo el caso cruzado con una complejidad $\Theta(n \log n)$.
- **Entregables:** Incluye algoritmos (`subarreglo.py`), pruebas de correctitud (`pruebas.py`), un script de medición de tiempos que genera gráficas comparativas (`medicion.py`) usando `matplotlib`, y un análisis teórico basado en el Teorema Maestro.