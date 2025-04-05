"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

def sortColors(arr): #O(n)
    white = 0
    red = 0
    blue = len(arr)-1

    while white<=blue:
        if arr[white]==0:
            arr[white],arr[red]=arr[red],arr[white]
            white = white + 1
            red = red + 1
        
        elif arr[white]==1:
            white = white + 1
        
        else:
            arr[white],arr[blue] = arr[blue],arr[white]
            blue = blue - 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)


#Psuedocode
"""
function sortColors(arr):
    initialize red = 0
    initialize white = 0
    initialize blue = length of arr -1

    while white<=blue:
        if arr[white]==0:
            swap arr[white] and arr[red]
            increment white
            increment red

        elif arr[white]==1:
            increment white
        else: # arr[white]==2
            swap arr[white] and arr[blue]
            decrement blue by 1

"""



