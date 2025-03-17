# return true is array comtains duplicate value 

#Brute force approach O(n*2)
# def is_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# arr = [1,2,3,4]

# print(is_duplicate(arr))

#Using Hashing set O(n)

def is_duplicate(arr):
    seen = set()

    # for i in arr:
    #     if i not in seen:   
    #         seen.add(i)
    #     elif i in seen:
    #         return True
    # return False

    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
arr = [1,2,3,4]

print(is_duplicate(arr))

