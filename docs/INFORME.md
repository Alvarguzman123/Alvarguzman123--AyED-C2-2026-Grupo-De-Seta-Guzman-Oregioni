# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas):
Elegimos el tema Pokedex principalmente por una cuestión de gustos,
nos pareció que armar un catálogo de Pokémon iba a hacer que el desarrollo 
del trabajo práctico sea mucho más llevadero, que hacer un recetario tradicional. 
Además, al conocer bien la franquicia, nos resulta muy intuitivo cargar los datos y pensar en sus atributos.


## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Un item en nuestro catálogo es un objeto de la clase "pokemon".

Atributos inmuntables: El "numero", el "nombre" y el "tipo".
Representan la identidad del objeto de forma estática, ya que una vez que es creado el pokemon, no tiene motivos para modificarse.

Atributos mutables: El atributo "evolucion".
Debe ser mutable obligatoriamente, ya que el sistema necesitará conectar de forma dinámica a los objetos en la memoria para las próximas entregas con el fin de armar la cadena evolutiva.


```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: imprimir_cadena_evolutiva(pokemon_actual)
- Caso base: si pokemon_actual.evolucion is None, se imprime "(última evolución)" y el recorrido termina.
- Caso recursivo: se imprime el nombre actual y se llama a imprimir_cadena_evolutiva(pokemon_actual.evolucion).
- Traza de un ejemplo real del dataset:

Traza para Bulbasaur
Paso 1: imprimir_cadena_evolutiva(bulbasaur)

¿Su evolución es None? No (es Ivysaur).

Acción: Imprime -> Bulbasaur. Llama a imprimir_cadena_evolutiva(ivysaur).

Paso 2: imprimir_cadena_evolutiva(ivysaur)

¿Su evolución es None? No (es Venusaur).

Acción: Imprime -> Ivysaur. Llama a imprimir_cadena_evolutiva(venusaur).

Paso 3: imprimir_cadena_evolutiva(venusaur)

¿Su evolución es None? SÍ (Caso base).

Acción: Imprime -> Venusaur (última evolución). Retorna y corta la recursión.

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | `insertar_al_inicio`, `insertar_al_final`, `insertar_ordenado`, `buscar`, `eliminar`, `tamanio`, `esta_vacia` | Los datos se conectan mediante nodos con referencias (no usa `list` de Python). El atributo tamaño siempre representa la cantidad real de nodos enlazados desde la cabeza. |
| Pila | `apilar`, `desapilar`, `ver_tope`, `esta_vacia` | Comportamiento LIFO (Último en entrar, primero en salir). Los elementos siempre se insertan y se retiran por el mismo extremo (la cabeza de la lista interna). |
| Cola | `encolar`, `desencolar`, `ver_frente`, `esta_vacia` | Comportamiento FIFO (Primero en entrar, primero en salir). Los elementos ingresan exclusivamente por el final de la lista interna y se retiran por el frente (la cabeza). |

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre los n elementos del catálogo una sola vez con un bucle for para imprimirlos. |
| Ver detalle de un ítem | O(n) | O(1) | Usa búsqueda lineal sobre el catálogo recorriendo de a uno hasta encontrar el Pokemon. |
| Búsqueda lineal | O(n) peor / O(1) mejor | O(1) | En el peor caso (no está o está al final) compara uno por uno los n elementos de la lista. |
| Búsqueda binaria | O(log n) | O(1) | Como la colección ya está ordenada, cada comparación descarta la mitad del rango restante. |
| Ordenar por selección | O(n^2) siempre | O(n) | Tiene dos bucles for anidados que siempre recorren todo el resto de la lista buscando el mínimo. Devuelve una copia de tamaño n. |
| Ordenar por inserción | O(n) mejor / O(n^2) peor | O(n) | Si ya está ordenado solo compara una vez por elemento; si está al revés desplaza todos los anteriores en cada paso. Devuelve una copia de tamaño n. |

Mediciones (`time.perf_counter`):

Se midieron los tiempos de ejecución reales comparando el catálogo original de la Pokédex (`n = 6`) contra una copia agrandada 100 veces (`n = 600`):

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal (nombre) | 6 | 0.000006 |
| búsqueda lineal (n x 100) | 600 | 0.000045 |
| búsqueda binaria (nombre) | 6 | 0.000006 |
| búsqueda binaria (n x 100) | 600 | 0.000005 |
| ordenar por selección (nombre) | 6 | 0.000013 |
| ordenar por selección (n x 100) | 600 | 0.024601 |

**Conclusión de las mediciones:** Al multiplicar el tamaño de la muestra por 100, se comprueba en la práctica que la búsqueda binaria (`O(log n)`) se mantiene casi constante sin importar el aumento de datos, la búsqueda lineal (`O(n)`) crece de forma proporcional y el ordenamiento por selección (`O(n^2)`) se dispara drásticamente por el costo de sus bucles anidados.

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
