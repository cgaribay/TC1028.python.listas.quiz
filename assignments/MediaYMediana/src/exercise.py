def media(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def mediana(lista):
    n = len(lista)
    lista.sort()
    if n % 2 == 0:
        return (lista[n // 2] + lista [n // 2 - 1]) / 2
    else:
        return float(lista[n // 2])

def main():
    num_elem = int(input())
    lista = []
    if num_elem > 0:
        for i in range(num_elem):
            lista.append(int(input()))
        print(f"Media: {media(lista)}")
        print(f"Mediana: {mediana(lista)}")
    else:
        print('Error')
    

if __name__=='__main__':
    main()
