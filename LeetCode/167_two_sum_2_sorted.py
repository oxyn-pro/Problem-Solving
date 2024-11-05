# TC: O(n)
# SC: O(1)
def two_sum(numbers, target):
    left = 1
    right = len(numbers)

    while left < right:
        if numbers[left - 1] + numbers[right - 1] > target:
            right -= 1
        elif numbers[left - 1] + numbers[right - 1] < target:
            left += 1
        else:
            return [left, right]


numbers = [2, 7, 11, 15]
target = 9
two_sum(numbers, target)
