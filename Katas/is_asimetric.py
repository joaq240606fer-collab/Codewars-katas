def esAntisimetrica(matriz):



if __name__ == __main__:
# Casos Test:

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print esAntisimetrica([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print esAntisimetrica(matriz4)
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

print esAntisimetrica(matriz5)
#>>>False 