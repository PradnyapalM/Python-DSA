# def has_long_prefix(arr):
#     res = ""

#     for i in range(len(arr[0])):
#         for s in arr:
#             print(s[0])
#             # print(s[2])
#             # print(arr[0][2])
#             if s[i]!=arr[0][i]:
#                 return res
#         res = res + arr[0][i]
#     return res
 

# # strs = ["flower", "flow", "flight"]
# strs = ["dog", "Car", "flight"]
# print(has_long_prefix(strs))

# strs = ["dog", "Car", "flight"] 
# for i in range(len(strs[0])):
#     for s in strs:
#         print(strs[0][1])
#         print("s[0]",s[1])

def hasPrfix(arr):
    res = ""

    for i in range (len(arr[0])):
        for s in arr:
            if s[i]!=(arr[0][i]):
                return res
        res = res + arr[0][i]
    return res
        

strs = ["flower","flow","flight"]
print(hasPrfix(strs))


# Psuedo code
"""
FUNCTION hasPrefix(arr):
    res ← empty string

    FOR i FROM 0 TO length of arr[0]:
        FOR each string s IN arr:
            IF s[i] ≠ arr[0][i]:
                RETURN res  // Mismatch found, return prefix so far

        res ← res + arr[0][i]  // Character matched in all strings

    RETURN res  // Entire prefix matched

"""


