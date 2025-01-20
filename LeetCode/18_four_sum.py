nums = [1, 0, -1, 0, -2, 2]
target = 0


# TC: O(n^3)
# SC: O(k)
def fourSum_hs(nums, target):
    """Solution using HashSet"""
    res = set()
    nums.sort()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left, right = j + 1, len(nums) - 1
            while left < right:
                sm = nums[i] + nums[j] + nums[left] + nums[right]

                if sm < target:
                    left += 1
                elif sm > target:
                    right -= 1
                else:
                    res.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1

    return [list(i) for i in res]


fourSum_hs(nums, target)


# TC: O(n^3)
# SC: O(k)
def fourSum(nums, target):
    """Even though both my solutions have the same time and space complexity, the current solution is faster."""
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1

            while left < right:
                sm = nums[i] + nums[j] + nums[left] + nums[right]

                if sm < target:
                    left += 1
                elif sm > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

    return res


fourSum(nums, target)


nums = [1, 0, -1, 0, -2, 2]
target = 0
k = 4


# TC: O(n^k) - in our example it will be O(n^4)
# SC: O(n^k) - in our example it will be O(n^4) because of the call stack
def kSum(nums, target):
    nums.sort()
    res, quad = [], []

    if len(nums) < 4:
        return res

    def rec(k, start, target):
        if k == 2:
            left, right = start, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

            return

        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue

            quad.append(nums[i])
            rec(k - 1, i + 1, target - nums[i])
            quad.pop()

        return

    rec(4, 0, target)
    return res


kSum(nums, target)
