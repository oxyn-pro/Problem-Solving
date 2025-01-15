# TC: O(n)
# SC: O(1) - XOR cancels out duplicates
def singleNumber(nums):
    res = 0

    for num in nums:
        res ^= num

    return res


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
