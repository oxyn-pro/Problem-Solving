# TC: O(n)
# SC: O(1)
def find_max(nums, k):
    maxx = 0
    left = 0
    max_avg = float("-inf")

    for right in range(len(nums)):
        maxx += nums[right]
        if k == right - left + 1:
            avg = maxx / k
            max_avg = max(max_avg, avg)
            maxx -= nums[left]
            left += 1

    return max_avg


# TC: O(n)
# SC: O(1)
def find_max_double(nums, k):
    """Just named as 'double' for distinction"""
    maxx = 0

    for i in range(k):
        maxx += nums[i]

    max_avg = maxx / k

    for right in range(k, len(nums)):
        maxx += nums[right]
        maxx -= nums[right - k]

        avg = maxx / k
        max_avg = max(max_avg, avg)

    return max_avg


nums = [1, 12, -5, -6, 50, 3]
k = 4
find_max_double(nums, k)
