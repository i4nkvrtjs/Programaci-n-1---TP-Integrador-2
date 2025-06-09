import time
import random
import sys

#Aumento de límite de recursión

sys.setrecursionlimit(5000)

#Ordenamiento

def bubble_sort(lista, clave):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][clave] > lista[j + 1][clave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista, clave):
    lista = lista.copy()
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual[clave] < lista[j][clave]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def selection_sort(lista, clave):
    lista = lista.copy()
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j][clave] < lista[min_idx][clave]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
    mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
    return quick_sort(menores, clave) + [pivote] + quick_sort(mayores, clave)

#Busqueda

def busqueda_lineal(lista, clave, valor):
    return [x for x in lista if x[clave].lower() == valor.lower()]

def busqueda_binaria(lista, clave, valor):
    izquierda = 0
    derecha = len(lista) - 1
    resultados = []
    valor = valor.lower()  # Normalizar el valor una sola vez

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista[medio][clave].lower()  # Normalizar el campo a comparar

        if actual == valor:
            # Encontrar el primer y último índice con el mismo valor
            inicio = medio
            fin = medio

            # Búsqueda binaria hacia la izquierda
            low = izquierda
            high = medio - 1
            while low <= high:
                mid = (low + high) // 2
                if lista[mid][clave].lower() == valor:
                    inicio = mid
                    high = mid - 1
                else:
                    low = mid + 1

            # Búsqueda binaria hacia la derecha
            low = medio + 1
            high = derecha
            while low <= high:
                mid = (low + high) // 2
                if lista[mid][clave].lower() == valor:
                    fin = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # Agregar todos los resultados de una vez
            resultados = lista[inicio : fin + 1]
            break

        elif actual < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return resultados

#Generación automática de listas de distintos tamaños

def generar_lista_canciones(n):
    nombres = ["Canción" + str(i) for i in range(n)]
    artistas = ["Artista" + str(i % 10) for i in range(n)]
    generos = ["Pop", "Rock", "Jazz", "Rap", "Clásica", "Indie"]
    return [
        {"nombre": random.choice(nombres), "artista": random.choice(artistas), "genero": random.choice(generos)}
        for _ in range(n)
    ]

#Ejecución

def mostrar_resultados(titulo, resultados):
    print(f"\n{titulo} ({len(resultados)} resultados):")
    for c in resultados[:10]:
        print(f" - {c['nombre']}, {c['artista']}, {c['genero']}")
    if len(resultados) > 10:
        print("...")

def ejecutar_busquedas(valor_busqueda, lista):
    campos = ["nombre", "artista", "genero"]
    ordenamientos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
    }

    print("\n=== BÚSQUEDA LINEAL ===")
    for campo in campos:
        inicio = time.perf_counter()
        resultado = busqueda_lineal(lista, campo, valor_busqueda)
        fin = time.perf_counter()
        mostrar_resultados(f"Lineal por {campo}", resultado)
        print(f"Tiempo búsqueda lineal: {fin - inicio:.8f} segundos")

    print("\n=== BÚSQUEDA BINARIA (CON ORDENAMIENTO) ===")
    for nombre_algoritmo, algoritmo in ordenamientos.items():
        print(f"\n--- {nombre_algoritmo.upper()} ---")
        for campo in campos:
            inicio_ordenamiento = time.perf_counter()
            lista_ordenada = algoritmo(lista, campo)
            fin_ordenamiento = time.perf_counter()

            inicio_busqueda = time.perf_counter()
            resultado = busqueda_binaria(lista_ordenada, campo, valor_busqueda)
            fin_busqueda = time.perf_counter()

            mostrar_resultados(f"Binaria por {campo}", resultado)
            print(f"Ordenamiento: {fin_ordenamiento - inicio_ordenamiento:.8f} s")
            print(f"Búsqueda:     {fin_busqueda - inicio_busqueda:.8f} s")

#Menu 

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Buscar")
        print("2. Salir")
        opcion = input("Elegí una opción (1 o 2): ").strip()

        if opcion == "1":
            try:
                tam = int(input("¿Cuántas canciones incluimos en la lista? (10, 100, 1000, 10000): "))
                if tam not in [10, 100, 1000, 10000]:
                    raise ValueError
                lista = generar_lista_canciones(tam)
                valor = input("Ingresá nombre, artista o género para buscar: ")
                ejecutar_busquedas(valor, lista)
            except ValueError:
                print("Elegí un número válido.")

        elif opcion == "2":
            print("¡Adiós!")
            break

        else:
            print("Opción inválida.")

#Start 

if __name__ == "__main__":
    menu()