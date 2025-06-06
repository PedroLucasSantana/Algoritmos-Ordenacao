def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivô = lista[0]

    menores = [x for x in lista[1:] if x < pivô]
    iguais = [x for x in lista if x == pivô]
    maiores = [x for x in lista[1:] if x > pivô]

    return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [10, 5, 2, 3, 7, 6, 8, 9, 1, 4]
ordenada = quick_sort(lista)
print("Lista ordenada:", ordenada)
