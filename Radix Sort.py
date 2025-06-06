def radix_sort(arr):
    max_num = max(arr)
    exp = 1 

    while max_num // exp > 0:
        counting_sort_por_digito(arr, exp)
        exp *= 10 

def counting_sort_por_digito(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    for i in range(n):
        índice = (arr[i] // exp) % 10
        count[índice] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        índice = (arr[i] // exp) % 10
        output[count[índice] - 1] = arr[i]
        count[índice] -= 1

    for i in range(n):
        arr[i] = output[i]

lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(lista)
print("Lista ordenada:", lista)
