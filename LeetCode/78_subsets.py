# TC: O(2^n) to be more precise it is O(n * 2^n) where n is copying a subset
# SC: O(2^n) to be more precise it is O(n * 2^n) where n is copying a subset
def subsets(nums):
    res = []
    sub = []

    def dfs(i):
        if i >= len(nums):
            res.append(sub.copy())
            return

        sub.append(nums[i])
        dfs(i + 1)

        sub.pop()
        dfs(i + 1)

    dfs(0)
    return res


nums = [1, 2, 3]
subsets(nums)
