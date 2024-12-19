# TC: O(n)
# SC: O(n)
def containsDuplicate(nums):
    hset = set()
    for num in nums:
        if num in hset:
            return True
        hset.add(num)
    return False


nums = [1, 2, 3, 1]
containsDuplicate(nums)
