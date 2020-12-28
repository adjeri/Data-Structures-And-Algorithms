def mergeSort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(mergeSort(left), mergeSort(right),array)

def merge(left, right,arr):
    i = j = k = 0
    # Copy data to temp arrays L[] and R[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


numbers = [99, 77, 89, 5, 2, 4, 5, 0, 4, 5, 6, 44, 5, 10,104]

print(mergeSort(numbers))
