def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia, no usa sorted."""
    nueva = list(coleccion)
    n = len(nueva)

    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if clave(nueva[j]) < clave(nueva[pos_min]):
                pos_min = j
        nueva[i], nueva[pos_min] = nueva[pos_min], nueva[i]

    return nueva


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""
    nueva = list(coleccion)

    for i in range(1, len(nueva)):
        actual = nueva[i]
        j = i - 1
        while j >= 0 and clave(nueva[j]) > clave(actual):
            nueva[j + 1] = nueva[j]
            j -= 1
        nueva[j + 1] = actual

    return nueva