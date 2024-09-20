import math

def combustible() -> None:
    n = int(input()) 
    m = int(input())

    l = 3  
    km_por_litro = 13 / 3
    capacidad_tanque = 70 

    litros_necesarios = m / km_por_litro

    if litros_necesarios <= n:
        print("llego")
    else:
        litros_faltantes = litros_necesarios - n
        recargas = math.ceil(litros_faltantes / capacidad_tanque)
        print(recargas)

if __name__ == '__main__':
    combustible()
