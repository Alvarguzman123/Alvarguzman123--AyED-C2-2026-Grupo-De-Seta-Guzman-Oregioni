# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).


| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | E1 | Elegir opción 1 (Listar catálogo) | N/A | imprime la lista de 6 Pokémon, sin error | no corrido | |
| P02 | E1 | Elegir una opción pendiente | tipear "2" | imprime "Todavía no está implementado" | no corrido | |
| P03 | E2 | Opción 5: recursión sobre elementos iniciales con cadena | Bulbasaur | imprime la cadena hacia Ivysaur y Venusaur | no corrido | |
| P04 | E2 | Opción 5: recursión sobre elementos finales en la lista | Venusaur | imprime solo a Venusaur (caso base) | no corrido | |
| P05 | E2 | Opción 5: recursión con elemento vacío | None | imprime "El pokemon no existe" sin colgarse | no corrido | |
| P06 | E2 | Elegir una opción de menú inexistente | tipear "99" | imprime "Opción inválida" y sigue el menú | no corrido | |
| P07 | E2 | Pasar enter vacío en el menú principal | enter | el programa no se rompe; vuelve a preguntar | no corrido | |
| P08 | E2 | Salir del programa con opción 0 | tipear "0" | imprime "Chau." y finaliza | no corrido | |