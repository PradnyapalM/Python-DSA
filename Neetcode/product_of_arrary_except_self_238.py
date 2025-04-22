'''
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit
 in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


def productExceptSelf(nums):
    n = len(nums)
    prefix_product = 1
    postfix_product = 1
    result = [0]*n

    for i in range(n):
        result[i]=prefix_product
        prefix_product = prefix_product * nums[i]

    for i in range(n-1,-1,-1):
        result[i] = result[i] * postfix_product
        postfix_product = postfix_product * nums[i]
        
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))

'''
Psuedocode

Function productExceptSelf(nums):
    n ← length of nums
    prefix_product ← 1
    postfix_product ← 1
    result ← array of size n filled with 0

    # First pass: calculate prefix product
    For i from 0 to n - 1:
        result[i] ← prefix_product
        prefix_product ← prefix_product × nums[i]

    # Second pass: calculate postfix product
    For i from n - 1 down to 0:
        result[i] ← result[i] × postfix_product
        postfix_product ← postfix_product × nums[i]

    Return result

'''
