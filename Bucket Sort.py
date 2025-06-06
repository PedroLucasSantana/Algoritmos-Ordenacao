def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(bucket_count * num)
        if index == bucket_count:  
            index = bucket_count - 1
        buckets[index].append(num)

    for i in range(bucket_count):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Arreglo ordenado:", sorted_arr)
