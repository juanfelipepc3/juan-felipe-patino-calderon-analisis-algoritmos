import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def test_subarreglo_maximo():
    # 1. Serie de ocho días de la situación problema (suma 17)
    serie_problema = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie_problema)[2] == 17
    assert subarreglo_maximo(serie_problema, 0, len(serie_problema) - 1)[2] == 17

    # 2. Serie de un solo elemento
    serie_un_elemento = [42]
    assert subarreglo_fuerza_bruta(serie_un_elemento)[2] == 42
    assert subarreglo_maximo(serie_un_elemento, 0, len(serie_un_elemento) - 1)[2] == 42

    # 3. Serie con todos los valores negativos
    serie_negativa = [-5, -2, -9, -1, -3]
    assert subarreglo_fuerza_bruta(serie_negativa)[2] == -1
    assert subarreglo_maximo(serie_negativa, 0, len(serie_negativa) - 1)[2] == -1

    # 4. Serie con todos los valores positivos
    serie_positiva = [1, 2, 3, 4, 5]
    assert subarreglo_fuerza_bruta(serie_positiva)[2] == 15
    assert subarreglo_maximo(serie_positiva, 0, len(serie_positiva) - 1)[2] == 15

    # 5. Caso donde el mejor tramo cruza el punto medio
    serie_cruzada = [1, -5, 4, 6, -3, 2] # punto medio es índice 2 (valor 4). Mejor es 4, 6 (suma 10).
    # Ah, wait, len=6. Medio = (0+5)//2 = 2.
    # Izq: 1, -5, 4. Der: 6, -3, 2. Cruzado: 4 + 6 = 10. Correcto.
    assert subarreglo_fuerza_bruta(serie_cruzada)[2] == 10
    assert subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1)[2] == 10

    # 6. Al menos veinte listas aleatorias
    random.seed(42)
    for _ in range(20):
        tamano = random.randint(5, 50)
        serie_aleatoria = [random.randint(-100, 100) for _ in range(tamano)]
        suma_fb = subarreglo_fuerza_bruta(serie_aleatoria)[2]
        suma_dv = subarreglo_maximo(serie_aleatoria, 0, len(serie_aleatoria) - 1)[2]
        assert suma_fb == suma_dv, f"Fallo en lista aleatoria: {serie_aleatoria}. FB: {suma_fb}, DV: {suma_dv}"

    print("Todas las pruebas pasaron exitosamente.")

if __name__ == "__main__":
    test_subarreglo_maximo()
