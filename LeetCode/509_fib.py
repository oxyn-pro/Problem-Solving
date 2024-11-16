# TC: O(2^n) - In the worst scenario, each branch will have 2 branches
# SC: O(n) - Call stack is linear
def fib_rec(n):
    """Unoptimized Recursive solution with 2 branches"""
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


fib_rec(5)


# TC: O(n)
# SC: O(n)
def fib_dp_mem(n):
    """Top to Bottom Dynamic Programming - Memoization"""
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]

        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]

    return f(n)


fib_dp_mem(5)


# TC: O(n)
# SC: O(n)
def fib_dp_tab(n):
    """Bottom Up Dynamic Programming - Tabulation"""
    tab = n * [0]

    for i in range(len(tab)):
        if i <= 1:
            tab[i] = i
        else:
            tab[i] = tab[i - 1] + tab[i - 2]


fib_dp_tab(5)
