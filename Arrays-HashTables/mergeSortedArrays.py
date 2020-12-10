def mergeSortedArrays(arr1, arr2):
    mergedArray = []
    
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)

    if n1 == 0:
        return arr2
    if n2 == 0:
        return arr1

    while i < n1 and j < n2:

        if arr1[i] < arr2[j] :
                mergedArray.append(arr1[i])
                i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1

    #remaining elements
    while i < n1:
        mergedArray.append(arr1[i])
        i += 1

    while j < n2:
        mergedArray.append(arr2[j])
        j += 1

    return mergedArray

print(mergeSortedArrays([0,3,4,31],[4,6,30]))