# TC: O(n)
# SC: O(n)
def two_sum(nums, target):
    dictt = {}
    for i in range(len(nums)):
        if (target - nums[i]) in dictt:
            return [dictt[target - nums[i]], i]
        dictt[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)
