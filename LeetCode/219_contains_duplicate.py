nums = [1, 2, 3, 1, 2, 3]
k = 2


def contains_nearby_duplicate(nums, k):
    dictt = {}
    for i in range(len(nums)):
        if nums[i] in dictt:
            if abs(i - dictt[nums[i]]) <= k:
                return True
        dictt[nums[i]] = i
    return False


contains_nearby_duplicate(nums, k)
