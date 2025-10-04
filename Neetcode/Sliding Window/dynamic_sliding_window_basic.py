# Neetcode Video
# Find the length of the longest subarray with the same value in each position
# (Duplicte with same Value)


"""

# Dynamic sliding window using For Loop O(n)
def longestSubarray(nums):
    left = 0
    right = 0
    length = 0
    for right in range(len(nums)):
        if nums[left]!=nums[right]:
            left = right
        length = max(length, right-left+1)
    return length

nums = [4,2,2,3,3,3]
print(longestSubarray(nums))

"""
"""

# Dynamic sliding window using While Loop 
def longestSubarray(nums):
    left = 0
    right = 0
    length = 0

    while right<len(nums):
        if nums[left]!=nums[right]:
            left = right
        length = max(length, right-left+1)
        right = right + 1
    return length

nums = [4,2,2,3,3,3,3]
print(longestSubarray(nums))

"""

# Q2 Find the Minimum length subarray where the sum is greator than or equal to
#  target assume all the values are positive

# Time Complexity O(n)
def shortestArrayLength(nums, target):
    left = 0
    right = 0
    length = float("inf")
    total = 0
    while right < len(nums):
        total =  total + nums[right]

        while total>=target:
            length = min(right-left+1, length)
            total = total - nums[left]
            left = left + 1
        right = right + 1
    return length

nums = [2,3,1,2,4,3]
target = 6
print(shortestArrayLength(nums, target))