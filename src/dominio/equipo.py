from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class Equipo:
    def __init__(self, tope=6):
        self._pokemones = ListaEnlazada()
        self._tope = tope

    def agregar(self, pokemon):
        # Verificamos si llegamos al límite usando el método tamanio()
        if self._pokemones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"El equipo está lleno (máximo {self._tope}).")
        
        # Si hay lugar, lo agregamos al final de la lista enlazada
        self._pokemones.insertar_al_final(pokemon)

    def eliminar(self, pokemon):
        self._pokemones.eliminar(pokemon)

    def listar(self):
        # Acá estamos usando automáticamente el __iter__ (yield) que armamos en lista_enlazada.py
        if self._pokemones.esta_vacia():
            print("El equipo está vacío.")
            return
            
        print("\n--- Tu Equipo Pokémon ---")
        for p in self._pokemones:
            print(f" -> {p}")