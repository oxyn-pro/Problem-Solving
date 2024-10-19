nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def remove_duplicates(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


remove_duplicates(nums)
