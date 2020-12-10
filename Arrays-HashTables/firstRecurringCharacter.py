def firstRecurringCharacter(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            return arr[i]
        else:
            dict[arr[i]] = True
    return 'nothing'

print(firstRecurringCharacter([1,3,6,4,5,10,10]))
