nums = [1, 2, 1]

# There are definitely more solutions to this problem but I have only included 3 of them.
# The third solution concat3 is food for thought...


def concat1(nums):
    return nums + nums


def concat2(nums):
    return nums * 2


def concat3(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans


concat3(nums)
