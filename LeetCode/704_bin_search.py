# TC: O(log n)
# SC: O(1)
def bin_search(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        elif mid_val > target:
            right = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
bin_search(nums, target)
