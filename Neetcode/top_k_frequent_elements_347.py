"""
Given an integer array nums and an integer k, 
return 
the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

#My solution using set and count 1 O(n*n)
# def frequentElement(nums,k):
#     res = set()
#     for i in nums:
#         # print("i", i)
#         counter = nums.count(i)
#         if counter>=k:
#             res.add(i)
#             # print(res)
#     return res

# nums = [1,1,1,2,2,3]
# k = 2
# print(frequentElement(nums,k))

# My solution 2 O(m+n)
# def frequentElement(nums,k):
#     count = {}
#     res = []
#     for x in nums:
#         count[x] = count.get(x,0)+1
    
#     for index, value in count.items():
#         if value>=k:
#             res.append(index)
#     return res


# nums = [1,1,1,2,2,3]
# k = 2
# print(frequentElement(nums,k))

# Solution 3 Using Bucket sort O(n) || NC

def topKFrequnet(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for x in nums:
        count[x] = count.get(x,0) + 1

    for index, value in count.items():
        freq[value].append(index)

    # print(freq)
    # freq = [[], [3], [2], [1], [], [], []] # index represents the frequency
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res
            
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequnet(nums,k))         
