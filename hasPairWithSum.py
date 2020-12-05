def hasPairWithSum(arr, sum):
    mySet = set()
    length = len(arr)
    for i in range(length):
        if arr[i] in mySet:
            return True
        mySet.add(sum - arr[i])
    return False

print(hasPairWithSum([6,4,1,2,3,7],9))