def selectionSort(array):
    length = len(array)
    for i in range(length-1):
        smallest = array[i]
        index = i
        for j in range(i + 1, length):
            if array[j] < smallest:
                smallest = array[j]
                index = j
        array[index] = array[i]
        array[i] = smallest

    return array

numbers = [99, 77, 89, 5, 2, 4, 5, 0, 4, 5, 6, 44, 5, 10,104]

print(selectionSort(numbers))