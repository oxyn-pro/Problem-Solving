import heapq


nums = [3, 2, 1, 5, 6, 4]
k = 3
k = len(nums) - k


# TC: O(n^2) But on average it is O(n) (Bit Theta)
# SC: O(n) But on average it is O(log n) because of the call stack
def k_largest(nums, s, e):
    """Use QuickSelect Algorithm"""
    pivot = nums[e]
    left = partition(nums, s, e, pivot)

    if k < left:
        return k_largest(nums, s, left - 1)
    elif k > left:
        return k_largest(nums, left + 1, e)
    else:
        return nums[left]


def partition(nums, s, e, pivot):
    left = s

    for i in range(s, e):
        if nums[i] <= pivot:
            temp = nums[left]
            nums[left] = nums[i]
            nums[i] = temp
            left += 1

    nums[e] = nums[left]
    nums[left] = pivot

    return left


k_largest(nums, s=0, e=len(nums) - 1)


# TC: O(n log k). O(n) - goes through each "number", log k - pushing/popping
# SC: O(k) - stores at most  k  elements
def findKthLargest_min_heap(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 3
findKthLargest_min_heap(nums, k)
