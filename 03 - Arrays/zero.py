def arreglos():
    arr = [-4, -2, 1, 4, 8]
    zero = float('inf')

    for i in arr:
        valor_abs = abs(i)
        print(f'{valor_abs}')

        if valor_abs < zero:
            zero = valor_abs

    print(f' # El valor mas cercano a 0 es: {zero}')

if __name__ == '__main__':
    arreglos()

