# Q Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# solution using hashmap
# from collections import defaultdict
# def groupAnagrams(strs): #O(m*n)
#     ans = defaultdict(list)
#     for s in strs:
#         count = [0]*26
#         for c in s:
#             count[ord(c)-ord("a")] = count[ord(c)-ord("a")]+1
#         ans[tuple(count)].append(s)
#     return ans.values()

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(strs))

#sudo code for above program
# import default dict
# ans = defaultdict(list)
# for s in strs:
    # count = [0]*26 (to calculate ordinal value) 
    # for c in s:
        # count[ord(c)-ord("a")] = count[ord(c)-ord("a")] + 1
    # ans[tuple(count)].append(s)(every string will append based on the key )
# return ans




# # BruteForce solution using sorted and hashmap
# from collections import defaultdict
# def groupAnagrams(strs):
#     ans = defaultdict(list)
#     for s in strs:
#         key = "".join(sorted(s))
#         ans[key].append(s)
#     return ans.values()

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(strs))


