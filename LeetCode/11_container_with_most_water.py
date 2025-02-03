height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


# TC: O(n)
# SC: O(1)
def maxArea(height):
    res = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


maxArea(height)
