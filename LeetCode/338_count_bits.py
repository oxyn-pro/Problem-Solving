n = 2


# TC: O(n log n) - Loop (n) * (log n) Because >> "right shifting" operator divides by 2
# SC: O(n)
def countBits(n):
    result = []
    for i in range(n + 1):
        count = 0
        while i > 0:
            if i & 1 == 1:
                count += 1
            i = i >> 1

        result.append(count)
    return result


countBits(n)


# TC: O(n)
# SC: O(n)
def countBits_dp(n):
    """Dynamic Programming - Bottom Up (Tabulation)"""
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp


countBits_dp(n)
