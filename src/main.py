from src.config import TEMA
from src.dominio.catalogo import pokedex_inicial, imprimir_cadena_evolutiva, bulbasaur, charmander, venusaur
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError, ItemNoEncontradoError
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def obtener_nombre(pokemon):
    return pokemon.nombre.lower()


def obtener_numero(pokemon):
    return pokemon.numero


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} - AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Equipo Pokemon")
    print("7. Eliminar último pokemon del equipo (pila)")
    print("8. Cola de combate (cola)")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    catalogo = list(pokedex_inicial)
    ordenado_por_nombre = False

    equipo = Equipo(tope=6)
    historial = Pila()
    cola_turnos = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
            print("\n--- Catálogo Pokédex ---")
            for pokemon in catalogo:
                print(pokemon)

        elif opcion == "2":
            print("\n--- Ver Detalle ---")
            nombre_buscado = input("Ingresá el nombre del Pokémon: ").strip().lower()
            encontrado = busqueda_lineal(catalogo, nombre_buscado, obtener_nombre)
            if encontrado is not None:
                print(f"Detalle encontrado: {encontrado}")
            else:
                print("No se encontró ese Pokémon en el catálogo.")

        elif opcion == "3":
            print("\n--- Opción 3: Buscar Pokémon ---")
            print("Buscar por: 1) Nombre (lineal)  2) Nombre (binaria)")
            tipo_busqueda = input("> ").strip()

            if tipo_busqueda == "1":
                nombre_buscado = input("Ingresá el nombre a buscar: ").strip().lower()
                encontrado = busqueda_lineal(catalogo, nombre_buscado, obtener_nombre)
                if encontrado is not None:
                    print(f"Encontrado (lineal): {encontrado}")
                else:
                    print("No encontrado en el catálogo.")

            elif tipo_busqueda == "2":
                if not ordenado_por_nombre:
                    catalogo = ordenar_insercion(catalogo, obtener_nombre)
                    ordenado_por_nombre = True
                    print("Aviso: Catálogo ordenado automáticamente por nombre para usar búsqueda binaria.")

                nombre_buscado = input("Ingresá el nombre a buscar: ").strip().lower()
                encontrado = busqueda_binaria(catalogo, nombre_buscado, obtener_nombre)
                if encontrado is not None:
                    print(f"Encontrado (binaria): {encontrado}")
                else:
                    print("No encontrado en el catálogo.")
            else:
                print("Opción de búsqueda inválida.")

        elif opcion == "4":
            print("\n--- Opción 4: Ordenar Catálogo ---")
            print("Ordenar por: 1) Nombre  2) Número")
            criterio = input("> ").strip()

            print("Algoritmo: 1) Selección (no estable)  2) Inserción (estable)")
            algoritmo = input("> ").strip()

            if criterio == "1":
                funcion_clave = obtener_nombre
                nombre_criterio = "nombre"
                ordenado_por_nombre = True
            elif criterio == "2":
                funcion_clave = obtener_numero
                nombre_criterio = "número"
                ordenado_por_nombre = False
            else:
                print("Criterio inválido.")
                continue

            if algoritmo == "1":
                catalogo = ordenar_seleccion(catalogo, funcion_clave)
                print(f"Catálogo ordenado por {nombre_criterio} (usando Selección).")
            elif algoritmo == "2":
                catalogo = ordenar_insercion(catalogo, funcion_clave)
                print(f"Catálogo ordenado por {nombre_criterio} (usando Inserción).")
            else:
                print("Algoritmo inválido.")
                continue

            for pokemon in catalogo:
                print(pokemon)

        elif opcion == "5":
            print("\n--- Probando cadena desde bulbasaur ---")
            imprimir_cadena_evolutiva(bulbasaur)

            print("\n--- Probando cadena con ítem inexistente ---")
            imprimir_cadena_evolutiva(None)

            print("\n--- Probando cadena desde venusaur ---")
            imprimir_cadena_evolutiva(venusaur)
            print()

        elif opcion == "6":
            print("\n--- Opción 6: Equipo Pokémon ---")
            nombre = input("Ingresá el nombre del Pokémon para agregar: ").strip()
            try:
                equipo.agregar(nombre)
                print(f"¡{nombre} agregado al equipo!")
                historial.apilar(nombre)
            except ColeccionLlenaError as e:
                print(f"ERROR: {e}")

            equipo.listar()

        elif opcion == "7":
            print("\n--- Opción 7: Historial (Pila - Deshacer) ---")
            try:
                pokemon_deshecho = historial.desapilar()
                print(f"Deshacer exitoso: se eliminó a {pokemon_deshecho} del historial.")
                equipo.eliminar(pokemon_deshecho)
            except PilaVaciaError as e:
                print(f"ERROR: {e}")

        elif opcion == "8":
            print("\n--- Cola de Combates (Turnos) ---")
            accion = input("¿(E)nviar a la cola de espera o (L)lamar al siguiente pokemon a combatir? ").strip().upper()

            if accion == "E":
                nombre = input("Nombre del Pokémon que se anota para pelear: ").strip()
                cola_turnos.encolar(nombre)
                print(f"[{nombre}] quedó anotado y espera su turno en la fila de combate.")

            elif accion == "L":
                try:
                    retador = cola_turnos.desencolar()
                    print(f"¡Llamando a la arena! Es el turno de combatir para: {retador}")
                except ColaVaciaError as e:
                    print(f"ERROR: {e}")

        elif opcion == "9":
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
    
#python -m src.main