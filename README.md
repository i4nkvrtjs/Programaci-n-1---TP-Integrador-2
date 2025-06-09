# Programación 1 TP Integrador 2

Valentín Piñeyro - Danilo Peirano

El objetivo principal del trabajo es evaluar el rendimiento de distintos algoritmos como Bubble Sort, Insertion Sort, Selection Sort, Quick Sort, y las búsquedas lineal y binaria, aplicados a listas de distinto tamaño. Se busca comprender el impacto del tamaño de datos y la elección del algoritmo en el tiempo de ejecución, así como validar los conceptos aprendidos en un contexto práctico.

El programa hecho en Python permite comparar el rendimiento de diferentes algoritmos de ordenamiento y algoritmos de búsqueda aplicados sobre una lista de canciones generadas aleatoriamente. Evalúa su eficiencia a través de tiempos de ejecución y muestra los resultados por consola.
En el repositorio, tanto como en la carpeta digital, se puede encontrar la documentación completa del código, la cual explica detalladamente su funcionamiento.

Como reflexiones, el trabajo nos aportó la capacidad de determinar con seguridad qué algoritmo funcionará mejor para distintos tipos de sistemas. Por ejemplo, si bien la búsqueda lineal es más lenta en todos los casos que la búsqueda binaria, a la segunda hay que sumarle el tiempo que toma el ordenamiento, con lo cuál, en bases de datos pequeñas, sería mejor utilizar la búsqueda lineal. Otra reflexión posible al respecto, es que si se piensan hacer varias búsquedas consecutivas, con ordenar la lista una sola vez la búsqueda binaria funcionaría, sin duda, con mayor velocidad.Por ende, el tiempo de ordenamiento sería rápidamente compensado, ya que al ejecutar varias búsquedas lineales seguidas, el tiempo que tarda se acumularía demasiado.
