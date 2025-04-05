# Given an array if the sum of arr equal to the target return
# their indices.

#Brute Force approch 
# def two_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]+arr[j]==target:
#                 return i,j
#     return []

# arr=[4,6,4,2,8]
# target = 14
# print(two_sum(arr,target))

# Using HashMap onePass{}

def two_sum(arr, target):
    pre_map = {}
    for i,v in enumerate(arr):
        diff = target - v
        if diff in pre_map:
            return(pre_map[diff], i)
        pre_map[v]=i
    return []

arr=[4,6,4,2,8]
target = 14
print(two_sum(arr,target))

# Sudo code for above solution

# def two_sum(arr, target):
#     pre_map = {}
#     for i, v in enumerate(arr):
#         calulate diff = target - v
#         if diff in pre_map then:
#             return(pre_map[diff], i)
#         else pre_map[v]=i
#     return

def two_sum(arr, target):
    prev_map={}
    for i,v in enumerate(arr):
        diff = target-v
        if diff in prev_map:
            print(prev_map)
            print("diff",prev_map[diff])
            return(prev_map[diff],i)
        prev_map[v]=i
        print(prev_map)
    return 

arr=[4,5,4,2,7]
target = 8
print(two_sum(arr,target))


#Psuedo code

"""
FUNCTION TwoSum(arr, target):
    pre_map = empty {}

    for each index, value in enumrate(arr):
            deff = target-value

            if diff EXISTS in prev_map:
                RETURN [pre_map[diff], index] // found the pair

            pre_map[value] = index // Save current value at this index

    RETURN empty list [] //No value found
"""