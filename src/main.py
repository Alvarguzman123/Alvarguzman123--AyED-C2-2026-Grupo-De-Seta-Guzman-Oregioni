from src.config import TEMA
from src.dominio.catalogo import pokedex_inicial, imprimir_cadena_evolutiva, bulbasaur, charmander, venusaur

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
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

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
            
            print("\n--- Probando cadena desde charmander ---")
            imprimir_cadena_evolutiva(charmander)

            print("\n--- Probando cadena desde venusaur ---")
            imprimir_cadena_evolutiva(venusaur)
            print()
                
        elif opcion in {"2", "3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
