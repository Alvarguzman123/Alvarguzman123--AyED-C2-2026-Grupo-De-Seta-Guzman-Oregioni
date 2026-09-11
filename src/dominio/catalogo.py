# Importamos la clase pokemon#
from src.dominio.pokemon import Pokemon

# Creamos los objetos que incluyen las cadenas evolutivas #
bulbasaur = Pokemon(1, "Bulbasaur", "Planta/Veneno")
ivysaur = Pokemon(2, "Ivysaur", "Planta/Veneno")
venusaur = Pokemon(3, "Venusaur", "Planta/Veneno")


#Hacemos lo mismo para la cadena evolutiva de Charmander#
charmander = Pokemon(4, "Charmander", "Fuego")
charmeleon = Pokemon(5, "Charmeleon", "Fuego")
charizard = Pokemon(6, "Charizard", "Fuego/Volador")

# Creamos el catálogo en forma de lista para cada grupo de pokemones #
pokedex_inicial = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard]
