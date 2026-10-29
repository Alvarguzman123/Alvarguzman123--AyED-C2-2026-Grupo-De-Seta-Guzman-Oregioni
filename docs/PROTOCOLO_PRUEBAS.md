# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).


| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | E1 | Elegir opción 1 (Listar catálogo) | N/A | imprime la lista de 6 Pokémon, sin error | pasa | |
| P02 | E1 | Elegir una opción pendiente | tipear "9" | imprime "Todavía no está implementado..." | pasa | |
| P03 | E2 | Opción 5: recursión sobre elementos iniciales con cadena | Bulbasaur | imprime la cadena hacia Ivysaur y Venusaur | pasa | |
| P04 | E2 | Opción 5: recursión sobre elementos finales en la lista | Venusaur | imprime solo a Venusaur (caso base) | pasa | |
| P05 | E2 | Opción 5: recursión con elemento vacío | None | imprime "El pokemon no existe" sin colgarse | pasa | |
| P06 | E2 | Elegir una opción de menú inexistente | tipear "99" | imprime "Opción inválida." y sigue el menú | pasa | |
| P07 | E2 | Pasar enter vacío en el menú principal | enter | el programa no se rompe; vuelve a preguntar | pasa | |
| P08 | E2 | Salir del programa con opción 0 | tipear "0" | imprime "Chau." y finaliza | pasa | |
| P09 | E3 | Agregar a la colección hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa | |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa | |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa | |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa | |
| P13 | E4 | Búsqueda lineal de un nombre que existe | Opción 3 -> 1 -> "charmander" | lo encuentra y lo muestra | pasa | |
| P14 | E4 | Búsqueda lineal de un nombre que no existe | Opción 3 -> 1 -> "mewtwo" | "No encontrado en el catálogo.", sin traceback, el menú sigue | pasa | |
| P15 | E4 | Búsqueda binaria con el catálogo desordenado | Opción 3 -> 2 -> "bulbasaur" | avisa que reordena automáticamente y lo encuentra | pasa | |
| P16 | E4 | Ordenar por un criterio y después por otro | Opción 4 por Nombre (1) y luego por Número (2) | el orden cambia correctamente en ambos casos | pasa | |