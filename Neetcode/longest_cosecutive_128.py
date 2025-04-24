"""
Given an unsorted array of integers nums, return the length 
of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

# My solution O(n*2)

# def longSeq(nums):
#     num_list = list(set(nums))
#     res = [1,]
#     for i in num_list:
#         if i+1 in num_list:
#             res.append(i+1)
#     return len(res)

# nums = [1,0,1,2]
# print(longSeq(nums))


#Solution Using neetcode Hashset O(n)

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in num_set:
            length = 0
            while (n+length) in num_set:
                length = length + 1
            longest = max(length,longest)
    return longest


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))