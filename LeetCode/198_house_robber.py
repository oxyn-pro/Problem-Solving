nums = [2, 7, 9, 3, 1]


# TC: O(2^n)
# SC: O(n)
def rob_td(nums):
    """Dynamic Programming - Top Down (Without Memoization)"""

    def dp(i):
        if i >= len(nums):
            return 0

        return max(nums[i] + dp(i + 2), dp(i + 1))

    return dp(0)


# TC: O(n)
# SC: O(n)
def rob_td_memo(nums):
    """Dynamic Programming - Top Down (Memoization)"""
    memo = {}

    def dp(i):
        if i >= len(nums):
            return 0
        elif i in memo:
            return memo[i]

        memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
        return memo[i]

    return dp(0)


# TC: O(n)
# SC: O(n)
def rob_bu_tb(nums):
    """Dynamic Programming - Buttom Up (Tabulation)"""
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]


# TC: O(n)
# SC: O(1)
def rob_bu(nums):
    """Dynamic Programming - Buttom Up (Pointers)"""
    if len(nums) == 1:
        return nums[0]

    prev_prev = nums[0]
    prev = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        temp = max(nums[i] + prev_prev, prev)
        prev_prev = prev
        prev = temp

    return prev
