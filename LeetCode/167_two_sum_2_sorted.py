# TC: O(n)
# SC: O(1)
def two_sum(numbers, target):
    left = 1
    right = len(numbers)

    while left < right:
        sm = numbers[left - 1] + numbers[right - 1]
        if sm > target:
            right -= 1
        elif sm < target:
            left += 1
        else:
            return [left, right]


numbers = [2, 7, 11, 15]
target = 9
two_sum(numbers, target)
