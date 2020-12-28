def quickSort(array, left, right):
    length = len(array)
    if left < right:
        pivot = right
        partition_index = partition(array, pivot, left, right)

        # sort left and right
        quickSort(array, left, partition_index - 1)
        quickSort(array, right, partition_index + 1)

    return array

def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, partition_index)
            partition_index += 1

    swap(array, right, partition_index)
    return partition_index

def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


numbers = [99, 77, 89, 5, 2, 4, 5, 0, 4, 5, 6, 44, 5, 10,104]

print(quickSort(numbers,0,len(numbers)-2))