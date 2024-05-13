def mostrar_matriz(matriz, fila, columna):
    if fila >= len(matriz) or columna >= len(matriz[0]):
        return
    print(matriz[fila][columna])
    if columna + 1 < len(matriz[0]):
        mostrar_matriz(matriz, fila, columna + 1)
    elif fila + 1 < len(matriz):
        mostrar_matriz(matriz, fila + 1, 0)


mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Mostrando la matriz:")
mostrar_matriz(mi_matriz, 0, 0)
