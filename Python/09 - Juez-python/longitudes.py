def dameLongitudes(v):
    arr_len = []
    
    for i in range(len(v)):
        arr_len.append(len(v[i]))

    print(f'{arr_len}')


if __name__ == '__main__':
    n = int(input())
    v = []

    for i in range(n):
        v.append(input()) 

    dameLongitudes(v)
