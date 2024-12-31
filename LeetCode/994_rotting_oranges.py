from collections import deque


# TC: O(n^2)
# SC: O(n^2)
def orangesRotting(grid):
    ROWS, COLS = len(grid), len(grid[0])
    queue = deque()
    visit = set()

    def bfs(r, c, mts):
        queue.append((r, c, mts))
        visit.add((r, c))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue:
            r, c, mts = queue.popleft()

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                continue

            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    print(r + dr, c + dc, mts + 1)
                    queue.append((r + dr, c + dc, mts + 1))
                    visit.add((r + dr, c + dc))
        return mts

    time = -1
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2 and (r, c) not in visit:
                time = bfs(r, c, 0)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visit:
                return -1

    return time - 1


grid = [[1, 2, 1], [0, 1, 1], [1, 1, 1]]
print(orangesRotting(grid))
