def arreglos():
    arr = [1, 2, 3, 4, 5, 6]
    minimo = arr[0]
    maximo = (len(arr) - 1)

    for i in arr:
        if i < minimo:
            minimo = i
        elif i > maximo:
            maximo = i
    
    print(f' # Minimo: {minimo} ')
    print(f' # Maximo: {maximo} ')

if __name__ == '__main__':
    arreglos()
