class Pokemon:
    def __init__(self, numero, nombre, tipo):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        #Sirve para establecer la relación de evolución entre los pokemones. Por ejemplo, Bulbasaur evoluciona a Ivysaur, y luego a Venusaur. Por ahora representa un valor nulo, pero luego se puede establecer la relación de evolución entre los pokemones.#
        self.evolucion = None

    def establecer_evolucion(self, siguiente_epokemon):
        self.evolucion = siguiente_epokemon
    def __str__(self):
        return f"Nro: {self.numero} | {self.nombre} | Tipo: {self.tipo}"