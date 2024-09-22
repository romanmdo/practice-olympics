lista = [2, 1, 3, 5, 4]
print(f'# Lista desordenada: {lista}')

## PARTICION DEL QUICKSORT
def particion(lista):
    pivote = lista[0]
    menor = []
    mayor = []

    for i in range(1, len(lista)): 
        if lista[i] < pivote:
            menor.append(lista[i])
        else:
            mayor.append(lista[i])

    return menor, pivote, mayor

## QUICKSORT
def quick_sort(lista):
    if len(lista) < 2:
        return lista 

    menor, pivote, mayor = particion(lista)
    return quick_sort(menor) + [pivote] + quick_sort(mayor)

lista_ordenada = quick_sort(lista)
print(f'# Lista ordenada: {lista_ordenada}')

## BUSQUEDA BINARIA
def busqueda_bin(lista, buscar):
    inicio = 0 # EL INICIO VA A SER EL PRIMER ELEMENTO DE LA LISTA 
    final = len(lista) - 1 # EL FINAL VA A SER LA CANTIDAD DE ELEMENTOS DE LA LISTA - 1

    while inicio <= final:
        medio = (inicio + final) // 2 # MITAD DE LA LISTA
        if lista[medio] == buscar: # SI EL ELEMETNO DEL MEDIO ES LO MISMO QUE EL ELEMENTO BUSCADO 
            return True
        elif lista[medio] < buscar: # SI EL ELEMENTO DEL MEDIO ES MENOR AL QUE BUSCAMOS
            inicio = medio + 1 
        elif lista[medio] > buscar: # SI EL ELEMENTO DEL MEDIO ES MAYOR AL QUE BUSCAMOS
            final = medio - 1
    return False

buscar = int(input(f'# Ingresa un numero que deseas buscar en la lista: '))
if busqueda_bin(lista_ordenada, buscar):
    print(f'# Encontre el numero! ')
else:
    print(f'# No encontre nada')
