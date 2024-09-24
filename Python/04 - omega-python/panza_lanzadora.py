def _main() -> None:
    n = int(input())
    arr_n = []

    cadena = input() 
    cadena = cadena.split(" ")
    arr_n = list(map(int, cadena))

    minimo = arr_n[0]
    maximo = arr_n[0]

    for i in range(1, n):
        if arr_n[i] < minimo:
            minimo = arr_n[i]
        if arr_n[i] > maximo:
            maximo = arr_n[i]

    print(f'{minimo} {maximo}')

if __name__ == '__main__':
    _main()