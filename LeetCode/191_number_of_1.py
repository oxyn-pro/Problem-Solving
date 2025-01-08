# TC: O(log n) - Because >> "right shifting" operator divides by 2
# SC: O(1)
def hammingWeight(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1

    return count


n = 11
hammingWeight(n)
