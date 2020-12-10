def twoSumIndexes(nums, target):
    # naive method
    # for i in range(len(nums)):
    #     rest = target - nums[i]
    #     j = i+1
    #     while j < len(nums):
    #         if nums[j] == rest:
    #             return [i, j]
    #         else:
    #             j += 1
    # return []

    # better method
    mydict = {}
    length = len(nums)
    for i in range(length):
        if nums[i] in mydict:
            return [mydict[nums[i]],i]
        mydict[target - nums[i]] = i
    return []

print(twoSumIndexes([3,2,10,4,8,14],24))