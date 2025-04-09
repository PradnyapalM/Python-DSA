# Q1. concatination of arrays
# def conc_array(nums):
#     return nums+nums

# nums=[1,2,1]
# print(conc_array(nums))

# Q2 Contains duplicate
# This is BruteForce approach
# def has_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# arr=[1,2,4,7,5,4]
# print(has_duplicate(arr))

# Using Hashing

# def has_duplicate(arr):
#     ans=set()
#     for i in arr:
#         if i in ans:
#             return True
#         ans.add(i)
#     return False

# arr=[1,2,4,7,5,4]
# print(has_duplicate(arr))

# Q3 Valid Anagrams
#using Bruteforce approach
# def has_anagram(s,t):
#     s=sorted(s)
#     t=sorted(t)
#     if s==t:
#         return True
#     return False

# s="jar"
# t="raj"
# print(has_anagram(s,t))

# using (dict)

# def has_anagrams(s,t):
#     if len(s)!=len(t):
#         return False
#     count={}
#     for x in s:
#         count[x]=count.get(x,0)+1

#     for x in t:
#         if x not in count or count[x]==0:
#             return False
#         count[x]=count[x]-1
#     return True

# s="jar"
# t="raj"
# print(has_anagrams(s,t))

# Q4 Two sum of array where target is 9
# BruteForce approach
# def two_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return [i,j]
#     return[]

# arr = [2,5,7,8]
# target=9

# print(two_sum(arr, target))

# using dict or hashmap

# def two_sum(arr, target):
#     pre_map = {}
#     for i,v in enumerate(arr):
#         diff = target-v
#         if diff in pre_map:
#             return [pre_map[diff], i]
#         pre_map[v]=i
#     return[]

# arr = [2,5,7,8]
# target=9

# print(two_sum(arr, target))

#sort an array


# def sort_array(arr):
#     for i in range (len(arr)):
#         for j in range (len(arr)):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j] = arr[j], arr[i]
#     return arr


# nums = [5,2,3,1]

# print(sort_array(nums))


# def TwoSum(arr, target):
#     pre_map = {}
#     for index,value in enumerate(arr):
#         diff = target-value
#         if diff in pre_map:
#             return [pre_map[diff], index]
#         pre_map[value] = index
#     return []

# nums = [2,5,7,9]
# target = 9
# print(TwoSum(nums, target))


# def MajorityElement(arr):
#     count = {}

#     for i in arr:
#         count = count.get(i,0)+1
        
#         if 
