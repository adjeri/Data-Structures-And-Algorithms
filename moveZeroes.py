def moveZeroes(nums):
    i = 0
    while i < len(nums) - 1:
        j = i+1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                swap = nums[i]
                nums[i] = nums[j]
                nums[j] = swap
                i += 1
            j+= 1
        i += 1
    print(nums)

moveZeroes([0,1,0,3,12])