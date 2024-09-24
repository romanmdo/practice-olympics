def suma(v):
    # Inicializamos la suma en 0 (un entero grande en Python)
    total_sum = 0
    
    # Iteramos por cada número en la lista y sumamos
    for num in v:
        total_sum += num
    
    # Retornamos la suma total
    return total_sum

if __name__ == '__main__':
    N = int(input())
    v = []
    for _ in range(N):
        v.append(int(input()))

    print(suma(v))
