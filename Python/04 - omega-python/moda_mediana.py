def suma() -> None:
    arr = []
    arr_map = []

    cadena = input()
    arr = cadena.split(" ")
    arr_map = list(map(int, arr))

    suma_1 = arr_map[0] + arr_map[3]
    suma_2 = arr_map[1] + arr_map[2]

    print(f'{suma_1} {suma_2}')

if __name__ == '__main__':
    suma()