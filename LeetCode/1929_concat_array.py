# There are definitely more solutions to this problem but I have only included 3 of them.
# The third solution concat3 is food for thought...


# TC: O(n)
# SC: O(n)
def concat1(nums):
    return nums + nums


# TC: O(n)
# SC: O(n)
def concat2(nums):
    return nums * 2


# TC: O(n)
# SC: O(n)
def concat3(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans


nums = [1, 2, 1]
concat3(nums)
