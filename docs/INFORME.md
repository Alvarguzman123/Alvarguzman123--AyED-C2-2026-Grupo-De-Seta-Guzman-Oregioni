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
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
