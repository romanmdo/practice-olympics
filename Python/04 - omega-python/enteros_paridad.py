def _main() -> None:
    arr_n = []
    
    arr_par = []
    arr_imp = [] 
    
    cadena = input() 
    cadena = cadena.split(" ")
    arr_n = list(map(int, cadena)) # Arreglo de str a ints

    p = int(input())

    for i in arr_n:
        if p == 0:
            if i % 2 == 0:
                arr_par.append(i)
        elif p == 1:
            if i % 2 == 1:
                arr_imp.append(i)

    if p == 0:
        print(f'{arr_par}')
    
    elif p == 1:
        print(f'{arr_imp}')

if __name__ == '__main__':
    _main()