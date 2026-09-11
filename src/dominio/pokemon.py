class pokemon:
    def __init__(self, numero, nombre, tipo):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        #Relación recursiva: Este atributo guarda otra instancia de pokemon, no un string  
        self.evolucion = None

    def set_evolucion(self, siguiente_pokemon):
        self.evolucion = siguiente_pokemon

    def __str__(self):
        return f"Nro: {self.numero} | {self.nombre} | Tipo: {self.tipo} "