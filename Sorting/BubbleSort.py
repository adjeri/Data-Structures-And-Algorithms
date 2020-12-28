def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

numbers = [99, 77, 89, 5, 2, 4, 5, 0, 4, 5, 6, 44, 5, 10]

print(bubbleSort(numbers))