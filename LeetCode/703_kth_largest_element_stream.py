# I wrote the necessary logic of the heap methods to reinforce my knowledge of HEAP.
# I am sure the code below can be written better.
class KthLargestManual:
    # TC: O(n log n) - heapify O(n) + Each heappop takes O(log n)
    # SC: O(k) - it stores heap
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums[:]
        self.heap = None

        self._heapify()
        while len(self.heap) > k + 1:
            self._heappop()

    def _heapify(self):
        if not self.nums:
            self.heap = [0]
            return

        self.nums.append(self.nums[0])
        self.heap = self.nums
        cur_node_idx = (len(self.heap) - 1) // 2

        while cur_node_idx > 0:
            i = cur_node_idx
            self._percolate_down(i)
            cur_node_idx -= 1

    def _heappop(self):
        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        self._percolate_down(i)
        return res

    def _percolate_down(self, i):
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[2 * i + 1] < self.heap[i]
            ):
                temp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                temp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i
            else:
                break

    def _heappush(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    # TC: O(log n) - heappush O(log n) + heappop O(log n)
    # SC: O(1)
    def add(self, val):
        self._heappush(val)

        if len(self.heap) > self.k + 1:
            self._heappop()

        return self.heap[1]


obj = KthLargestManual(3, [4, 5, 8, 2])
print(obj.add(3))

import heapq


class KthLargest:
    # TC: O(n log n) - heapify O(n) + Each heappop takes O(log n)
    # SC: O(k) - it stores heap
    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums

        heapq.heapify(nums)

        while self.k < len(self.nums):
            heapq.heappop(self.nums)

    # TC: O(log n) - heappush O(log n) + heappop O(log n)
    # SC: O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
