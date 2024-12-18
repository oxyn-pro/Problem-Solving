import heapq
import math


# TC: O(n log k). O(n) - goes through each "point", log k - pushing/popping
# SC: O(k) - stores at most  k  elements
def kClosest(points, k):
    x_origin = 0
    y_origin = 0

    def distance(x, y):
        return math.sqrt((x - x_origin) ** 2 + (y - y_origin) ** 2)

    heap = []
    for pts in points:
        heapq.heappush(heap, (-distance(pts[0], pts[1]), pts))
        while len(heap) > k:
            heapq.heappop(heap)

    return [pts for _, pts in heap]


points = [[1, 3], [-2, 2]]
k = 1
kClosest(points, k)
