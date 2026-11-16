from src.config import TEMA
from src.dominio.pokemon import Pokemon
from src.dominio.catalogo import (
    pokedex_inicial, imprimir_cadena_evolutiva, bulbasaur, charmander, 
    venusaur, armar_catalogo_desde_txt, filas_del_catalogo
)
from src.dominio.equipo import Equipo
from src.excepciones import (
    ColeccionLlenaError, PilaVaciaError, ColaVaciaError, 
    ItemNoEncontradoError, ArchivoInvalidoError
)
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.persistencia.texto import DATA, guardar_csv
from src.persistencia.binario import (
    guardar_binario, cargar_binario, alta_binario, baja_binario, actualizar_registro
)

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

RUTA_CSV = DATA / "pokedex.csv"
RUTA_BIN = DATA / "pokedex.bin"
ENCABEZADOS_CSV = ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa", "velocidad", "generacion"]

def obtener_nombre(pokemon):
    return pokemon.nombre.lower()


def obtener_numero(pokemon):
    return pokemon.numero

def posicion_del_numero(catalogo, num_buscado):
    """Devuelve la posición (0-based) del ítem en la lista, buscando por número."""
    for i, p in enumerate(catalogo):
        if p.numero == num_buscado:
            return i
    raise ItemNoEncontradoError(f"No hay Pokémon con número {num_buscado}")

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
            print("\n--- Opción 6: Gestión del Catálogo (ABM) y Equipo ---")
            print(" a) Agregar nuevo Pokémon al catálogo (Alta)")
            print(" b) Modificar Pokémon existente (Modificación)")
            print(" c) Eliminar Pokémon del catálogo (Baja)")
            print(" d) Agregar Pokémon al Equipo de Combate (Tope 6)")
            sub6 = input("> ").strip().lower()

            if sub6 == "a":
                try:
                    num = int(input("Número del nuevo Pokémon: "))
                    nom = input("Nombre: ").strip()
                    tip = input("Tipo: ").strip()
                    nuevo = Pokemon(num, nom, tip)
                    
                    catalogo.append(nuevo) # Lo metemos en memoria
                    
                    # Persistencia instantánea
                    alta_binario(RUTA_BIN, nuevo)
                    guardar_csv(RUTA_CSV, filas_del_catalogo(catalogo), ENCABEZADOS_CSV)
                    print(f"¡{nom} agregado al catálogo y guardado en los archivos!")
                except ValueError:
                    print("Error: El número debe ser un entero.")
                    
            elif sub6 == "b":
                try:
                    num = int(input("Número del Pokémon a modificar: "))
                    pos = posicion_del_numero(catalogo, num)
                    
                    print(f"Modificando a: {catalogo[pos].nombre}")
                    nom = input("Nuevo nombre: ").strip()
                    tip = input("Nuevo tipo: ").strip()
                    
                    # Actualizamos en memoria
                    catalogo[pos].nombre = nom
                    catalogo[pos].tipo = tip
                    
                    # Persistencia (acceso directo)
                    actualizar_registro(RUTA_BIN, pos, catalogo[pos])
                    guardar_csv(RUTA_CSV, filas_del_catalogo(catalogo), ENCABEZADOS_CSV)
                    print("¡Pokémon modificado con éxito!")
                except ValueError:
                    print("Error: Ingrese un número válido.")
                except ItemNoEncontradoError as e:
                    print(e)
                    
            elif sub6 == "c":
                try:
                    num = int(input("Número del Pokémon a eliminar: "))
                    pos = posicion_del_numero(catalogo, num)
                    
                    eliminado = catalogo.pop(pos) # Lo sacamos de memoria
                    
                    # Persistencia
                    baja_binario(RUTA_BIN, pos)
                    guardar_csv(RUTA_CSV, filas_del_catalogo(catalogo), ENCABEZADOS_CSV)
                    print(f"¡{eliminado.nombre} eliminado permanentemente!")
                except ValueError:
                    print("Error: Ingrese un número válido.")
                except ItemNoEncontradoError as e:
                    print(e)
                    
            elif sub6 == "d":
                nombre = input("Ingresá el nombre del Pokémon para agregar: ").strip()
                try:
                    equipo.agregar(nombre)
                    print(f"¡{nombre} agregado al equipo!")
                    historial.apilar(nombre)
                except ColeccionLlenaError as e:
                    print(f"ERROR: {e}")
                equipo.listar()
            else:
                print("Subopción inválida.")

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
            print("\n--- Guardar / Cargar Archivos ---")
            print(" a) Cargar catálogo desde CSV (.csv)")
            print(" b) Guardar catálogo en CSV (.csv)")
            print(" c) Guardar catálogo en binario (.bin)")
            print(" d) Cargar catálogo desde binario (.bin)")
            sub = input("> ").strip().lower()

            try:
                if sub == "a":
                    catalogo = armar_catalogo_desde_txt(RUTA_CSV)
                    print(f"¡Catálogo cargado! Ahora hay {len(catalogo)} Pokémon en memoria.")
                
                elif sub == "b":
                    filas = filas_del_catalogo(catalogo)
                    guardar_csv(RUTA_CSV, filas, ENCABEZADOS_CSV)
                    print("¡Catálogo guardado en pokedex.csv con éxito!")
                
                elif sub == "c":
                    guardar_binario(RUTA_BIN, catalogo)
                    print("¡Catálogo guardado en pokedex.bin con éxito!")
                    
                elif sub == "d":
                    catalogo = cargar_binario(RUTA_BIN)
                    print(f"¡Catálogo cargado desde binario! Ahora hay {len(catalogo)} Pokémon en memoria.")
                
                else:
                    print("Subopción inválida.")
                    
            except ArchivoInvalidoError as error:
                print(f"Error al leer el archivo: {error}")


if __name__ == "__main__":
    main()
    
#python -m src.main