from collections import deque


# TC: O(n * m)
# SC: O(n * m)
def numIslands(grid):
    """I implemented it with allocating space for the "visit" hashset"""
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c, visit):
        if (
            min(r, c) < 0
            or r == ROWS
            or c == COLS
            or (r, c) in visit
            or grid[r][c] == "0"
        ):
            return

        visit.add((r, c))

        dfs(r - 1, c, visit)
        dfs(r + 1, c, visit)
        dfs(r, c - 1, visit)
        dfs(r, c + 1, visit)

    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and not (r, c) in visit:
                count += 1
                dfs(r, c, visit)

    return count


def numIslands_bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    queue = deque()

    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def bfs():
        while queue:
            r, c = queue.popleft()

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                continue

            grid[r][c] = "0"

            for dr, dc in neighbors:
                if (r + dr, c + dc) != "0":
                    queue.append((r + dr, c + dc))

    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                count += 1
                queue.append((r, c))
                bfs()

    return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
numIslands(grid)


numIslands_bfs(grid)
