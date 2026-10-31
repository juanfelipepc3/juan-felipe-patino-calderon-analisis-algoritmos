"""Pruebas de verificacion para ListaEnlazada y TablaHash."""

import random
from estructuras import ListaEnlazada, TablaHash

# ---------------------------------------------------------------
# 1. Busqueda exitosa e infructuosa en la lista enlazada
# ---------------------------------------------------------------
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")
lista.insertar(1000000017, "en bodega")
lista.insertar(1000000005, "entregado")

assert lista.buscar(1000000010) == "en bodega"
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert lista.buscar(9999999999) is None
assert lista.buscar(0) is None
print("OK: busqueda exitosa e infructuosa en lista enlazada.")

# ---------------------------------------------------------------
# 2. Busqueda exitosa e infructuosa en la tabla hash
# ---------------------------------------------------------------
tabla = TablaHash(7)
tabla.insertar(1000000010, "en bodega")
tabla.insertar(1000000024, "en reparto")
tabla.insertar(1000000017, "en bodega")
tabla.insertar(1000000005, "entregado")

assert tabla.buscar(1000000010) == "en bodega"
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000005) == "entregado"
assert tabla.buscar(9999999999) is None
assert tabla.buscar(0) is None
print("OK: busqueda exitosa e infructuosa en tabla hash.")

# ---------------------------------------------------------------
# 3. Colision forzada: con m = 7, guias 10, 24 y 17 caen en casilla 3
# ---------------------------------------------------------------
tabla_col = TablaHash(7)
for guia in (10, 24, 17):
    tabla_col.insertar(guia, "en bodega")

# Verificar que las tres caen en la casilla 3
assert tabla_col.hash(10) == 3, f"10 % 7 = {tabla_col.hash(10)}, esperado 3"
assert tabla_col.hash(24) == 3, f"24 % 7 = {tabla_col.hash(24)}, esperado 3"
assert tabla_col.hash(17) == 3, f"17 % 7 = {tabla_col.hash(17)}, esperado 3"

# Verificar que las tres se pueden buscar despues de insertar
assert tabla_col.buscar(10) == "en bodega"
assert tabla_col.buscar(24) == "en bodega"
assert tabla_col.buscar(17) == "en bodega"

# Verificar que la lista de la casilla 3 tiene longitud 3
assert tabla_col.casillas[3].tamano == 3, (
    f"Longitud casilla 3: {tabla_col.casillas[3].tamano}, esperado 3"
)

# Verificar que una guia inexistente en la casilla 3 devuelve None
assert tabla_col.buscar(31) is None  # 31 % 7 == 3 pero no fue insertada
print("OK: colision forzada con m = 7 funciona correctamente.")

# ---------------------------------------------------------------
# 4. Factor de carga
# ---------------------------------------------------------------
assert tabla_col.factor_carga() == 3 / 7, (
    f"Factor de carga: {tabla_col.factor_carga()}, esperado {3/7}"
)
print("OK: factor_carga() correcto tras tres inserciones.")

# ---------------------------------------------------------------
# 5. Veinte colecciones aleatorias: lista y tabla devuelven lo mismo
# ---------------------------------------------------------------
rng = random.Random(42)

for i in range(20):
    n = rng.randint(50, 500)
    m = max(7, n // 2)
    guias = rng.sample(range(10**9, 10**10 - 1), n)
    estados = [rng.choice(["en bodega", "en reparto", "entregado"]) for _ in range(n)]

    lista_r = ListaEnlazada()
    tabla_r = TablaHash(m)

    for guia, estado in zip(guias, estados):
        lista_r.insertar(guia, estado)
        tabla_r.insertar(guia, estado)

    # Verificar busquedas existentes
    for guia, estado in zip(guias, estados):
        res_lista = lista_r.buscar(guia)
        res_tabla = tabla_r.buscar(guia)
        assert res_lista == estado, (
            f"Coleccion {i}: lista devolvio {res_lista} para guia {guia}, "
            f"esperado {estado}"
        )
        assert res_tabla == estado, (
            f"Coleccion {i}: tabla devolvio {res_tabla} para guia {guia}, "
            f"esperado {estado}"
        )

    # Verificar busquedas inexistentes
    inexistentes = []
    while len(inexistentes) < 10:
        guia_inex = rng.randint(10**9, 10**10 - 1)
        if guia_inex not in guias:
            inexistentes.append(guia_inex)

    for guia_inex in inexistentes:
        res_lista = lista_r.buscar(guia_inex)
        res_tabla = tabla_r.buscar(guia_inex)
        assert res_lista is None, (
            f"Coleccion {i}: lista devolvio {res_lista} para guia inexistente "
            f"{guia_inex}"
        )
        assert res_tabla is None, (
            f"Coleccion {i}: tabla devolvio {res_tabla} para guia inexistente "
            f"{guia_inex}"
        )

print(f"OK: 20 colecciones aleatorias, lista y tabla coinciden siempre.")

# ---------------------------------------------------------------
print("\n=== Todas las pruebas pasaron correctamente. ===")
