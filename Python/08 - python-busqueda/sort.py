lista = [2, 1, 3, 5, 4]
print(f'Lista desordenada: {lista}')

def particion(lista):
    pivot = lista[0]
    menor = []
    mayor = []

    for i in range(1, len(lista)): # ITERA DESDE UN RANGO DE 1 HASTA EL FINAL DE LA LISTA
        if lista[i] < pivot:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return menor, pivot, mayor  # DEVUELVE LAS 3 LISTAS 


def quick_sort(lista):
    if len(lista) < 2: # CASO BASE
        return lista 

    menor, pivot, mayor = particion(lista)
    return quick_sort(menor) + [pivot] + quick_sort(mayor)

print(f'Lista ordenada: {quick_sort(lista)}')