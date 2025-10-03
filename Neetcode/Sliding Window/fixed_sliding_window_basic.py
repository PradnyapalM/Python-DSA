# Neetcode video

# Q contains duplicate in an array [1,2,3,2,3,3] where k=2
# return true of there two elements wiithin window


def contains_duplicate(nums, k):
    left = 0
    right = 0
    window = set()

    while right < len(nums):
        if right-left + 1 > k:
            window.remove(nums[left])
            left = left + 1
        if nums[right] in window:
            return True
        window.add(nums[right])
        right = right + 1
    return False

nums = [1,2,3,2,3]
k=2

print(contains_duplicate(nums, k))
