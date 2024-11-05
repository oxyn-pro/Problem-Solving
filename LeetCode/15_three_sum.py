# TC: O(n^2)
# SC: O(n)
def threeSum(nums):
    res = []
    nums.sort()  # O(n log n)

    # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)):  # O(n^2)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sm = nums[i] + nums[left] + nums[right]
            if 0 < sm:
                right -= 1
            elif 0 > sm:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
threeSum(nums)
