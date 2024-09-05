def arreglos():
    arr = [1, 2, 2, 3, 4, 5, 6]
    
    search = int(input(f' # Ingresa un numero para buscar sus ocurrencias: '))
    cont = 0

    for i in arr:
        if search == i:
            cont = cont + 1
    
    print(f' # El numero {search}, se repite {cont} veces en el arreglo')

if __name__ == '__main__':
    arreglos()
