nums = [5, 2, 3, 1]


# TC: O(n^2)
# SC: O(1)
def bubble_srt(nums):
    """Bubble Sort - Stable"""
    arr_len = len(nums)
    for i in range(arr_len):
        swapped = False
        for j in range(arr_len - i - 1):
            if nums[j + 1] < nums[j]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp

                swapped = True
        if not swapped:
            break

    return nums


bubble_srt(nums)


# TC: O(n^2)
# SC: O(1)
def selection_srt(nums):
    """Selection Sort - Unstable"""
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


selection_srt(nums)


# TC: O(n^2)
# SC: O(1)
def insertion_srt(nums):
    """Insertion Sort - Stable"""
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]
            j -= 1
    return nums


insertion_srt(nums)


# TC: O(n log n)
# SC: O(n)
def merge_srt(nums, s, e):
    """Merge Sort - Two Pointer"""
    if (e - s) + 1 <= 1:
        return nums

    m = (s + e) // 2

    # Sort the left half
    merge_srt(nums, s, m)
    # Sort the right half
    merge_srt(nums, m + 1, e)

    _merge(nums, s, m, e)

    return nums


def _merge(nums, s, m, e):
    left = nums[s : m + 1]  # Copy the Left half of the main array
    right = nums[m + 1 : e + 1]  # Copy the Right half of the main array

    i = 0  # For the Left half of the array
    j = 0  # For the Right half of the array
    k = s  # Actual index of the main array that helps us update the values

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


merge_srt(nums, s=0, e=len(nums) - 1)
