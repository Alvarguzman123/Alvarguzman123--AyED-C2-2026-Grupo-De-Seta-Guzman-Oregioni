from src.config import TEMA
from src.dominio.catalogo import pokedex_inicial, imprimir_cadena_evolutiva, bulbasaur, charmander, venusaur
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError, ItemNoEncontradoError
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return
   




TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

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
            print("\n--- Pokédex Inicial ---")
            for pokemon in pokedex_inicial:
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
                
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

    
#python -m src.main