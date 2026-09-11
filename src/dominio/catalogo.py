# Importamos la clase pokemon#
from src.dominio.pokemon import Pokemon

# Creamos los objetos que incluyen las cadenas evolutivas #
bulbasaur = Pokemon(1, "Bulbasaur", "Planta/Veneno")
ivysaur = Pokemon(2, "Ivysaur", "Planta/Veneno")
venusaur = Pokemon(3, "Venusaur", "Planta/Veneno")

# Conectamos con las evoluciones #
bulbasaur.set_evolucion(ivysaur)
ivysaur.set_evolucion(venusaur)

#Hacemos lo mismo para la cadena evolutiva de Charmander#
charmander = Pokemon(4, "Charmander", "Fuego")
charmeleon = Pokemon(5, "Charmeleon", "Fuego")
charizard = Pokemon(6, "Charizard", "Fuego/Volador")

charmander.set_evolucion(charmeleon)
charmeleon.set_evolucion(charizard)

# Creamos el catálogo en forma de lista para cada grupo de pokemones #
pokedex_inicial = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard]


# Función recursiva obligatoria (Requisito 3.3 del TP)
def imprimir_cadena_evolutiva(pokemon_actual):
    # Caso base explícito: si no pasamos ningún pokemon, cortamos la recursión
    if pokemon_actual is None:
        return
    
    print(f" -> {pokemon_actual.nombre}")
    
    # Llamada recursiva: volvemos a ejecutar la función, pero pasándole la evolución
    imprimir_cadena_evolutiva(pokemon_actual.evolucion)

bulbasaur