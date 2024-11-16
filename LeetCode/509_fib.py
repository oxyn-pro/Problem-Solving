# TC: O(2^n) - In the worst scenario, each branch will have 2 branches
# SC: O(n) - Call stack is linear
def fib_td(n):
    """Top-Down Dynamic Programming - No Memoization"""
    if n <= 1:
        return n
    return fib_td(n - 1) + fib_td(n - 2)


fib_td(5)


# TC: O(n)
# SC: O(n)
def fib_td_mem(n):
    """Top-Down Dynamic Programming - Memoization"""
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]

        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]

    return f(n)


fib_td_mem(5)


# TC: O(n)
# SC: O(n)
def fib_bu_tab(n):
    """Bottom-Up Dynamic Programming - Tabulation"""
    tab = (n + 1) * [0]

    for i in range(len(tab)):
        if i <= 1:
            tab[i] = i
        else:
            tab[i] = tab[i - 1] + tab[i - 2]

    return tab[i]


fib_bu_tab(5)


# TC: O(n)
# SC: O(1)
def fib_bu_var(n):
    """Bottom-Up Dynamic Programming - Variable"""
    if n <= 1:
        return n

    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur


fib_bu_var(5)
