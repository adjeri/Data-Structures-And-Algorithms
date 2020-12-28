def insertionSort(array):
    length = len(array)
    i = 0
    while i < length:
        for j in range(i):
            if array[i] < array[j]:
                smallest = array[i]
                for x in range(i, j, -1):
                    array[x] = array[x - 1]
                array[j] = smallest
        i += 1
    return array

numbers = [99, 77, 89, 5, 2, 4, 5, 0, 4, 5, 6, 44, 5, 10,104]

print(insertionSort(numbers))