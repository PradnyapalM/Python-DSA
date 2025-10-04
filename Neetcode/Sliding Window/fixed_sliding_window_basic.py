# Neetcode video

"""

# Q contains duplicate in an array [1,2,3,2,3,3] where k=2
# return true of there two elements wiithin window

# O(n)
def contains_duplicate(nums, k):
    left = 0
    right = 0
    window = set()

    while right < len(nums):
        if right-left + 1 > k:
            window.remove(nums[left])
            left = left + 1
        if nums[right] in window:
            return True
        window.add(nums[right])
        right = right + 1
    return False

nums = [1,2,3,2,3]
k=2

print(contains_duplicate(nums, k))
"""

"""
# Q2 sum of each window using sliding window pattern
i/p nums = [2,4,6,8,10]
window_size = 3
o/p [2,4,6] = 12
    [4,6,8] = 18
    [6,8,10] = 24
"""
# Time Complexity O(n)
def eachWindowSum(nums, k):

    left = 0 
    right = 0
    window = []
    current_sum = 0

    while right<len(nums):
        current_sum = current_sum + nums[right]
        if right-left+1>k:
            current_sum = current_sum - nums[left]
            left = left + 1
        if right - left + 1==k:
            window.append(current_sum)        
        right = right + 1
    return window

nums = [2,4,6,8,10]
k = 3
print(eachWindowSum(nums,k))

