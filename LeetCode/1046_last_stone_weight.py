import heapq


# TC: O(n log n)
# SC: O(n)
def lastStoneWeight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)

        if x == y:
            continue
        else:
            heapq.heappush(stones, x - y)

    stones.append(0)
    return abs(stones[0])


stones = [3, 7, 2]
lastStoneWeight(stones)
