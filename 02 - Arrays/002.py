def arreglos():
    arr = [1, 2, 3, 4, 5]
    suma = 0

    for i in arr:
        print(f'# Elemento: {i}')

        suma = i + suma

    print(f'# Su suma es: {suma}')

if __name__ == '__main__':
    arreglos()

