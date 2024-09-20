def arreglos():
    arr = [1, 2, 3, 4, 5]
    arr_reversed = []
    
    # Iterar sobre el arreglo desde el último elemento hasta el primero
    for i in range(len(arr) - 1, -1, -1):
        arr_reversed.append(arr[i])
    
    print(f'Original: {arr}')
    print(f'Reversed: {arr_reversed}')
    
if __name__ == '__main__':
    arreglos()
