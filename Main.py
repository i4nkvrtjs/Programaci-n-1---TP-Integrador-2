import time

# Base de datos de canciones
canciones = [
    {"nombre": "Imagine", "artista": "John Lennon", "genero": "Rock"},
    {"nombre": "Billie Jean", "artista": "Michael Jackson", "genero": "Pop"},
    {"nombre": "Smells Like Teen Spirit", "artista": "Nirvana", "genero": "Grunge"},
    {"nombre": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock"},
    {"nombre": "Hey Jude", "artista": "The Beatles", "genero": "Rock"},
    {"nombre": "Bad Guy", "artista": "Billie Eilish", "genero": "Pop"},
    {"nombre": "Thriller", "artista": "Michael Jackson", "genero": "Pop"},
]

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

#Busquedas

def busqueda_lineal(lista, clave, valor):
    return [x for x in lista if x[clave].lower() == valor.lower()]

def busqueda_binaria(lista, clave, valor):
    izquierda = 0
    derecha = len(lista) - 1
    resultados = []
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista[medio][clave].lower()
        if actual == valor.lower():
            i = medio
            while i >= 0 and lista[i][clave].lower() == valor.lower():
                resultados.insert(0, lista[i])
                i -= 1
            i = medio + 1
            while i < len(lista) and lista[i][clave].lower() == valor.lower():
                resultados.append(lista[i])
                i += 1
            break
        elif actual < valor.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return resultados

#Ejecución

def mostrar_resultados(titulo, resultados):
    print(f"\n{titulo} ({len(resultados)} resultados):")
    for c in resultados:
        print(f" - {c['nombre']} ({c['artista']}, {c['genero']})")

def ejecutar_busquedas(valor_busqueda):
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
        resultado = busqueda_lineal(canciones, campo, valor_busqueda)
        fin = time.perf_counter()
        mostrar_resultados(f"Lineal por {campo}", resultado)
        print(f"⏱ Tiempo búsqueda lineal: {fin - inicio:.8f} segundos")

    print("\n=== BÚSQUEDA BINARIA CON ORDENAMIENTO ===")
    for nombre_algoritmo, algoritmo in ordenamientos.items():
        print(f"\n--- Algoritmo de ordenamiento: {nombre_algoritmo.upper()} ---")
        for campo in campos:
            #Ordena una vez por campo
            inicio_ordenamiento = time.perf_counter()
            canciones_ordenadas = algoritmo(canciones, campo)
            fin_ordenamiento = time.perf_counter()
            tiempo_ordenamiento = fin_ordenamiento - inicio_ordenamiento

            #Busqueda binaria en lista ordenada
            inicio_busqueda = time.perf_counter()
            resultado = busqueda_binaria(canciones_ordenadas, campo, valor_busqueda)
            fin_busqueda = time.perf_counter()
            tiempo_busqueda = fin_busqueda - inicio_busqueda

            mostrar_resultados(f"Binaria por {campo}", resultado)
            print(f"⏱ Tiempo ordenamiento ({campo}): {tiempo_ordenamiento:.8f} s")
            print(f"⏱ Tiempo búsqueda binaria:     {tiempo_busqueda:.8f} s")


#Menu

def menu():
    while True:
        print("\n=== BUSCADOR DE CANCIONES ===")
        valor = input("🔍 Ingresá nombre, artista o género (o 'salir'): ").strip()
        if valor.lower() == "salir":
            break
        ejecutar_busquedas(valor)

#Start

if __name__ == "__main__":
    menu()
