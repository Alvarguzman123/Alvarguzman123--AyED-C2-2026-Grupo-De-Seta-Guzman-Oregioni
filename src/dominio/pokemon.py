class Pokemon:
    def __init__(self, numero, nombre, tipo):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"Nro: {self.numero} | {self.nombre} | Tipo: {self.tipo}"