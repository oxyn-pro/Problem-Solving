# TC: O(2^n) - In the worst scenario, each branch will have 2 branches
# SC: O(n) - Call stack is linear
def cs_td(n):
    """Top-Down Dynamic Programming - No Memoization"""
    if n == 0:
        return 1
    elif n < 0:
        return 0

    return cs_td(n - 1) + cs_td(n - 2)


cs_td(6)


# TC: O(n)
# SC: O(n)
def cs_td_mem(n):
    """Top-Down Dynamic Programming - Memoization"""
    memo = {0: 1}

    def f(x):
        if x < 0:
            return 0

        if x in memo:
            return memo[x]

        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]

    return f(n)


cs_td_mem(6)


# TC: O(n)
# SC: O(n)
def cs_bu_tab(n):
    """Bottom-Up Dynamic Programming - Tabulation"""
    tab = (n + 1) * [0]

    for i in range(len(tab)):
        if i <= 1:
            tab[i] = 1
        else:
            tab[i] = tab[i - 1] + tab[i - 2]

    return tab[i]


cs_bu_tab(6)


# TC: O(n)
# SC: O(1)
def cs_bu_var(n):
    """Bottom-Up Dynamic Programming - Variable"""
    prev = 1
    cur = 1

    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur


cs_bu_var(6)
