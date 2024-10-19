nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


def max_cons(nums, k):
    zeros = left = longest_window = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        longest_window = max(longest_window, right - left + 1)
    return longest_window


max_cons(nums, k)
