# TC: O(2^n) to be more precise it is O(n * 2^n) where n is copying a subset
# SC: O(2^n) to be more precise it is O(n * 2^n) where n is copying a subset
def combinationSum(candidates, target):
    res = []
    sub = []
    total = 0

    def dfs(i, sub, total):
        if total == target:
            res.append(sub.copy())
            return

        if i >= len(candidates) or total > target:
            return

        sub.append(candidates[i])
        dfs(i, sub, total + candidates[i])

        sub.pop()
        dfs(i + 1, sub, total)

    dfs(0, sub, total)
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
