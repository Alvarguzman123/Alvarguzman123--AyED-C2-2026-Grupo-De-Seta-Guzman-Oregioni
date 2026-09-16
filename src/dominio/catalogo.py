# Importamos la clase pokemon#
from src.dominio.pokemon import Pokemon

# Creamos los objetos que incluyen las cadenas evolutivas #
bulbasaur = Pokemon(1, "Bulbasaur", "Planta/Veneno")
ivysaur = Pokemon(2, "Ivysaur", "Planta/Veneno")
venusaur = Pokemon(3, "Venusaur", "Planta/Veneno")

# Establecemos la relación de evolución entre los pokemones #
bulbasaur.establecer_evolucion(ivysaur)
ivysaur.establecer_evolucion(venusaur)


#Hacemos lo mismo para la cadena evolutiva de Charmander#
charmander = Pokemon(4, "Charmander", "Fuego")
charmeleon = Pokemon(5, "Charmeleon", "Fuego")
charizard = Pokemon(6, "Charizard", "Fuego/Volador")

# Establecemos nuevamente la relación de evolución entre los pokemones #
charmander.establecer_evolucion(charmeleon)
charmeleon.establecer_evolucion(charizard)

# Creamos el catálogo en forma de lista para cada grupo de pokemones #
pokedex_inicial = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard]

def imprimir_cadena_evolutiva(pokemon_actual):
    if pokemon_actual is None:
        return
    print(f"-> {pokemon_actual.nombre}")

    imprimir_cadena_evolutiva(pokemon_actual.evolucion)
