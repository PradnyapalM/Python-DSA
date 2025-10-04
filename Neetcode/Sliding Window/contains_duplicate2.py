"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def ContainsDuplicate(nums,k):
    left = 0
    right = 0
    window = set()

    while right<len(nums):
        if right-left+1>k:
            window.remove(nums[left])
            left = left + 1
        if nums[right] in window:
            return True
        window.add(nums[right])
        right = right + 1
    return False

nums = [1,2,3,1,2,3]
k = 2
print(ContainsDuplicate(nums,k))