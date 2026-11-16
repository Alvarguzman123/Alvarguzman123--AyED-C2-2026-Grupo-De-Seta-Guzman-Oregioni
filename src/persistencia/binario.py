"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Ejemplo Pokédex:
  id          I
  nombre     20s
  tipo1      12s
  tipo2      12s
  hp          H
  ataque      H
  defensa     H
  velocidad   H
  generacion  H
"""
import struct
from pathlib import Path
from src.excepciones import ArchivoInvalidoError
from src.dominio.pokemon import Pokemon

FORMATO = struct.Struct("<I 20s 12s 12s 5H")
HEADER = struct.Struct("<4s 1s I")  # 9 bytes: magia (AYED), tema (P), cantidad
TEMA = b'P'

def _a_bytes(texto, ancho):
    """Texto -> bytes UTF-8 de 'ancho' exacto rellenado con nulos."""
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")

def _a_texto(datos):
    """Bytes -> texto sacando los nulos del final."""
    return datos.rstrip(b"\x00").decode("utf-8")

def _item_a_tupla(p):
    """Objeto Pokemon -> tupla para struct.pack."""
    return (
        p.numero,
        _a_bytes(p.nombre, 20),
        _a_bytes(p.tipo, 12),
        _a_bytes("", 12),  # tipo2 vacío
        0, 0, 0, 0, 1      # hp, ataque, defensa, velocidad en 0, generacion 1
    )

def _tupla_a_item(t):
    """Tupla de struct.unpack -> objeto Pokemon."""
    return Pokemon(
        numero=t[0],
        nombre=_a_texto(t[1]),
        tipo=_a_texto(t[2])
    )

def guardar_binario(ruta, items):
    """Escribe el archivo completo: header + registros."""
    ruta = Path(ruta)
    with ruta.open("wb") as archivo:
        # Escribimos el header con la cantidad actual de elementos
        archivo.write(HEADER.pack(b"AYED", TEMA, len(items)))
        
        # Escribimos cada Pokémon
        for item in items:
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def cargar_binario(ruta):
    """Lee el binario validando la magia y el tema. Devuelve una lista de Pokemon."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo binario: {ruta}")

    with ruta.open("rb") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Binario truncado: ni siquiera tiene header completo.")
            
        magia, tema, cantidad = HEADER.unpack(cabecera)
        
        if magia != b"AYED":
            raise ArchivoInvalidoError("Magia incorrecta: este archivo no es de este TP.")
        if tema != TEMA:
            raise ArchivoInvalidoError(f"El tema del archivo ({tema!r}) no coincide.")

        catalogo = []
        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError("Binario truncado: faltan registros.")
            catalogo.append(_tupla_a_item(FORMATO.unpack(datos)))
            
        return catalogo


def actualizar_registro(ruta, posicion, item):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""
    ruta = Path(ruta)
    with ruta.open("r+b") as archivo:
        # Saltamos el header y los registros anteriores directamente al byte que nos importa
        archivo.seek(HEADER.size + posicion * FORMATO.size)
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))

def alta_binario(ruta, item):
    """Agrega un registro AL FINAL y actualiza la cantidad del header."""
    ruta = Path(ruta)
    with ruta.open("r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        magia, tema, cantidad = HEADER.unpack(cabecera)
        
        archivo.seek(0, 2)  # Salta al FINAL del archivo
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))
        
        archivo.seek(0)     # Vuelve al principio para actualizar el número
        archivo.write(HEADER.pack(magia, tema, cantidad + 1))

def baja_binario(ruta, posicion):
    """Quita el registro 'posicion': relee, saca ese registro y reescribe todo."""
    ruta = Path(ruta)
    with ruta.open("r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        magia, tema, cantidad = HEADER.unpack(cabecera)
        
        # Leemos todos los registros
        registros = [archivo.read(FORMATO.size) for _ in range(cantidad)]
        
        # Borramos el que nos pidieron
        del registros[posicion]
        
        # Pisamos el archivo con la nueva lista
        archivo.seek(0)
        archivo.truncate()
        archivo.write(HEADER.pack(magia, tema, len(registros)))
        for datos in registros:
            archivo.write(datos)