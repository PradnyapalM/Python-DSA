"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not 
changed (for example, 2 and 3), while the positions of other numbers 
are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

"""

#Mysolution O(n*2)
# def sortArray(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr

# nums = [5,1,1,2,0,0]
# print(sortArray(nums))


#solution using merge sort O(nlogn)

def sortArray(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #recursion
        sortArray(left_arr)
        sortArray(right_arr)

        #merger/conqure
        i = 0
        j = 0
        k = 0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1
        
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1
        
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1

    return arr


nums = [5,1,1,2,0,0]
print(sortArray(nums))


#Psudo code
"""
FUNCTION sortArray(arr):
    IF length of arr > 1:
        mid ← length of arr divided by 2
        left_arr ← first half of arr
        right_arr ← second half of arr

        // Recursively sort both halves
        sortArray(left_arr)
        sortArray(right_arr)

        // Initialize pointers for merging
        i ← 0      // pointer for left_arr
        j ← 0      // pointer for right_arr
        k ← 0      // pointer for main arr

        // Merge left_arr and right_arr into arr
        WHILE i < length of left_arr AND j < length of right_arr:
            IF left_arr[i] < right_arr[j]:
                arr[k] ← left_arr[i]
                i ← i + 1
            ELSE:
                arr[k] ← right_arr[j]
                j ← j + 1
            k ← k + 1

        // Copy remaining elements of left_arr (if any)
        WHILE i < length of left_arr:
            arr[k] ← left_arr[i]
            i ← i + 1
            k ← k + 1

        // Copy remaining elements of right_arr (if any)
        WHILE j < length of right_arr:
            arr[k] ← right_arr[j]
            j ← j + 1
            k ← k + 1

    RETURN arr


"""            