def esCuadrada(matriz):
    n = len(matriz)
    return n == len(fila for fila in matriz)




def esAntisimetrica(matriz):
    if not esCuadrada:
        return False
    n = len(matriz)
    for f in range(n):
        for c in range(n):
            if matriz[f][c] != -matriz[c][f]:
                return False

    return True








    
                    
if __name__ == "__main__":
    # Casos Test:
    assert esAntisimetrica([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) is True
    # >>> True

    assert esAntisimetrica([[0, 1, 2], [-1, 0, -2], [2, 2, 3]]) is False
    # >>> False

    assert esAntisimetrica([[1, 2, 5], [0, 1, -9], [0, 0, 1]]) is False
# >>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (asser)
    matriz4 = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]]

    assert esAntisimetrica(matriz4) is False
# >>>False

    matriz5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz5) is False
# >>>False
