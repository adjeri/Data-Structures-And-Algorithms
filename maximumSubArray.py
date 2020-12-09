def maxSubArray(nums) -> int:
    left = 0
    right = len(nums) - 1
    return MaximumSum(nums,left,right)

def MaximumSum(nums,left,right):

    # If list contains only one element
    if right == left:
        return nums[left]

    # Find middle element of the list
    mid = (left + right) // 2

    # Find maximum sublist sum for the left sublist
    # including the middle element
    leftMax = float('-inf')
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += nums[i]
        if sum > leftMax:
            leftMax = sum

    # Find maximum sublist sum for the right sublist
    # excluding the middle element
    rightMax = float('-inf')
    sum = 0        # reset sum to 0

    for i in range(mid + 1, right + 1):
        sum += nums[i]
        if sum > rightMax:
            rightMax = sum

    # Recursively find the maximum sublist sum for left sublist
    # and right sublist and tale maximum
    maxLeftRight = max(MaximumSum(nums, left, mid), MaximumSum(nums, mid + 1, right))

    # return maximum of the three
    return max(maxLeftRight, leftMax + rightMax)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))