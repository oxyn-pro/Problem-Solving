# TC: O(n * m)
# SC: O(n * m)
def maxAreaOfIsland(grid):
    """I implemented it without allocating space for the "visit" hashset"""
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c):
        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
            return 0

        grid[r][c] = 0

        count = 1
        count += dfs(r - 1, c)
        count += dfs(r + 1, c)
        count += dfs(r, c - 1)
        count += dfs(r, c + 1)

        return count

    max_island = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                area = dfs(r, c)
                max_island = max(max_island, area)
    return max_island


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

maxAreaOfIsland(grid)
