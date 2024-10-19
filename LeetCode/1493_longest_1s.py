nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]


def longest_sub(nums):
    zeros = left = longest_window = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        longest_window = max(longest_window, right - left)
    return longest_window


longest_sub(nums)
