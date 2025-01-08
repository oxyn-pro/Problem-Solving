m = 3
n = 7


# TC: O(2^n)
# SC: O(n)
def uniquePaths_td(m, n):
    """Dynamic Programming - Top Down (Without Memoization)"""

    ROWS = m
    COLS = n

    def dp(r, c):
        if r == ROWS or c == COLS:
            return 0

        if r == ROWS - 1 and c == COLS - 1:
            return 1

        return dp(r + 1, c) + dp(r, c + 1)

    return dp(0, 0)


# TC: O(n)
# SC: O(n)
def uniquePaths_td_memo_hm(m, n):
    """Dynamic Programming - Top Down (Memoization using HashMap)"""

    ROWS = m
    COLS = n
    memo = {}

    def dp(r, c):
        if r == ROWS or c == COLS:
            return 0

        if (r, c) in memo:
            return memo[(r, c)]

        if r == ROWS - 1 and c == COLS - 1:
            return 1

        memo[(r, c)] = dp(r + 1, c) + dp(r, c + 1)
        return memo[(r, c)]

    return dp(0, 0)


# TC: O(n)
# SC: O(n)
def uniquePaths_td_memo_2d(m, n):
    """Dynamic Programming - Top Down (Memoization using Grid (2d Array))"""

    ROWS = m
    COLS = n
    grid_memo = [[0] * (COLS) for r in range(ROWS)]

    def dp(r, c):
        if r == ROWS or c == COLS:
            return 0

        if grid_memo[r][c] > 0:
            return grid_memo[r][c]

        if r == ROWS - 1 and c == COLS - 1:
            return 1

        grid_memo[r][c] = dp(r + 1, c) + dp(r, c + 1)
        return grid_memo[r][c]

    return dp(0, 0)


# TC: O(n)
# SC: O(n)
def uniquePaths_bu_tb(m, n):
    """Dynamic Programming - Bottom Up (Tabulation (2d Array))"""
    ROWS = m
    COLS = n
    grid = [[0] * (COLS) for r in range(ROWS)]

    for r in range(ROWS):
        grid[r][COLS - 1] = 1

    for c in range(COLS):
        grid[ROWS - 1][c] = 1

    for r in range(ROWS - 2, -1, -1):
        for c in range(COLS - 2, -1, -1):
            grid[r][c] = grid[r + 1][c] + grid[r][c + 1]

    return grid[0][0]


# TC: O(n)
# SC: O(1)
def uniquePaths_bu_tb(m, n):
    """Dynamic Programming - Bottom Up (Pointers)"""
    ROWS = m
    COLS = n

    prev_row = [0] * (COLS)

    for r in range(ROWS - 1, -1, -1):
        curr_row = [0] * (COLS)
        curr_row[COLS - 1] = 1
        for c in range(COLS - 2, -1, -1):
            curr_row[c] = prev_row[c] + curr_row[c + 1]

        prev_row = curr_row

    return curr_row[0]


uniquePaths_bu_tb(m, n)
