def matriz():
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]}', end=' ')
        print()  # Nueva línea después de cada fila

if __name__ == '__main__':
    matriz()
