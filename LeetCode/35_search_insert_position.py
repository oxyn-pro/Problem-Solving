# TC: O(log n)
# SC: O(1)
def search_insert(nums, target):
    h, l = len(nums) - 1, 0

    while l <= h:
        mid = (h + l) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid

        if mid_val > target:
            h = mid - 1
        elif mid_val < target:
            l = mid + 1

    return l


nums = [1, 3, 5, 7]
target = 6
search_insert(nums, target)
